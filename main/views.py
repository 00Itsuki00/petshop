from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product
from .forms import ProductForm




def index(request):
    products=Product.objects.all()
    return render(request, 'main/index.html', {"products":products})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'main/create_product.html', {'form': form})


def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('index')


def register_view(request):

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        print(f'username: {username}\npassword: {password}\nemail: {email}\nfirstname: {firstname}\nlastname: {lastname}')
        user = User.objects.create_user(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
        user.set_password(password)
        user.save()
        return redirect('index')
    return render(request, 'auth/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            print('welcome')
            return redirect('index')
        else:
            print('go away')
            return redirect('register')
    return render(request, 'auth/login.html')
def logout_view(request):
    logout(request)
    return redirect('index')



