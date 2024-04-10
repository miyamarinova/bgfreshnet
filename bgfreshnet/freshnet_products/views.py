from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from bgfreshnet.freshnet_products.forms import ProductCreateForm
from bgfreshnet.freshnet_products.models import FreshNetProduct

# Create your views here.

class ProductCreateView(views.CreateView):
    form_class = ProductCreateForm
    template_name = 'products/product-add-page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the profile details page of the current user
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.pk})

class AllProductsView(views.ListView):
    model = FreshNetProduct
    template_name = 'products/all-products.html'  # Specify the template name where you want to display the list
    context_object_name = 'products'  # Specify the context variable name to use in the template

class ProductDetailsView(views.DetailView):
    model = FreshNetProduct
    template_name = 'products/product-details.html'  # Specify the template for product details
    context_object_name = 'product'  # Specify the context variable name to use in the template
