from django.urls import path

from bgfreshnet.accounts.views import (FreshNetUserRegistrationView, LogInUserView, logout_user, vendor_admin,
                                       ProfileDetailsView, ProfileUpdateView, ProfileDeleteView)

urlpatterns = [
    path('register/', FreshNetUserRegistrationView.as_view(), name='register user'),
    path('login/', LogInUserView.as_view(), name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('vendor_admin/', vendor_admin, name='vendor home'),
    path('profiledetails/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profileupdate/', ProfileUpdateView.as_view(), name='profile update'),
    path('profiledelete/<int:pk>/', ProfileDeleteView.as_view(), name='delete profile')

]