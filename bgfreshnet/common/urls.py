from django.urls import path

from bgfreshnet.common.views import IndexView, AboutUsView, contact,thanks, like_product,comment_product,search_product
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aboutus/', AboutUsView.as_view(), name='about-us'),

    path('contactus/', contact, name='contact us'),
    path('contact/', thanks, name='thanks'),
    path('product_like/<int:pk>/', like_product, name='like product'),
    path('product_comment/<int:pk>/', comment_product, name='comment product'),

]