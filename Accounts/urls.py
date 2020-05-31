from django.urls import path
from . import views

urlpatterns = [
    path("Accounts/login", views.login, name='login'),
    path("Accounts/register", views.register, name= 'register'),
    path("Accounts/logout", views.logout, name='logout'),
    path("Accounts/profile",views.profile,name="profile")
    #path("Accounts/contact",views.contacts, name="contacts"),



]
