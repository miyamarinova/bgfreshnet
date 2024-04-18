from django.urls import path

from bgfreshnet.common.views import IndexView, AboutUsView, AllProducersView, contact,thanks
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aboutus/', AboutUsView.as_view(), name='about-us'),
    path('listproducers/', AllProducersView.as_view(), name='list producers'),
    path('contactus/', contact, name='contact us'),
    path('contact/', thanks, name='thanks')
]