from django.urls import path
from GuestApp import views


urlpatterns = [
path('Login/',views.Login,name='Login'),
path('login_process',views.login_process,name="login_process"),
path('',views.Guesthome,name='Guesthome'),
path('userRegistration/',views.userRegistration,name='userRegistration'),
path('filllocation1/',views.filllocation1,name='filllocation1'),
path('userRegistration_process/',views.userRegistration_process,name="userRegistration_process"),
path('sellerRegistration/',views.sellerRegistration,name='sellerRegistration'),
path('sellerRegistration_process/',views.sellerRegistration_process,name="sellerRegistration_process"),
path('Forgot_password/',views.Forgot_password,name="Forgot_password"),
path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
path('contact/',views.contact,name="contact"),
path('IndexG/',views.IndexG,name='IndexG'),

]