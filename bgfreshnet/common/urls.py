from django.urls import path

from bgfreshnet.common.views import IndexView, AboutUsView, AllProducersView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aboutus/', AboutUsView.as_view(), name='about-us'),
    path('listproducers/', AllProducersView.as_view(), name='list producers')
]