from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_product, name='create'),
    path('delete/<int:id>', views.delete_product, name='delete'),

]
