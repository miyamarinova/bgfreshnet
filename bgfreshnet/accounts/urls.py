from django.urls import path

from bgfreshnet.accounts.views import FreshNetUserRegistrationView, LogInUserView, logout_user

urlpatterns = [
    path('register/', FreshNetUserRegistrationView.as_view(), name='register user'),
    path('login/', LogInUserView.as_view(), name='login user'),
    path('logout/', logout_user, name='logout user')
]