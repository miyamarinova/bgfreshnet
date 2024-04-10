from django.urls import path
from bgfreshnet.freshnet_products.views import ProductCreateView, AllProductsView,ProductDetailsView

urlpatterns = [
    path('create-product/',  ProductCreateView.as_view(), name='create product'),
    path('all-products/', AllProductsView.as_view(), name='all products'),
    path('product-details/<int:pk>/', ProductDetailsView.as_view(), name='product-details')


]