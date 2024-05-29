from django.urls import path

from bgfreshnet.common.views import IndexView, AboutUsView, contact

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aboutus/', AboutUsView.as_view(), name='about-us'),
    path('contactus/', contact, name='contact us'),




]