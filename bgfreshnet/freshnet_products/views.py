from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from bgfreshnet.freshnet_products.decorators import admin_group_required, has_delete_permission
from bgfreshnet.freshnet_products.forms import ProductCreateForm, ProductBaseForm
from bgfreshnet.freshnet_products.models import FreshNetProduct
from django.utils.decorators import method_decorator
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

@method_decorator(admin_group_required, name='dispatch')
@method_decorator(user_passes_test(has_delete_permission), name='dispatch')
class EditProductView(views.UpdateView):
    model = FreshNetProduct
    form_class = ProductBaseForm
    template_name = 'products/edit-product.html'  # Update with your actual template name
    success_url = reverse_lazy('product-details')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.user or self.request.user.is_superuser

@method_decorator(admin_group_required, name='dispatch')
@method_decorator(user_passes_test(has_delete_permission), name='dispatch')
class DeleteProductView(views.DeleteView):
        model = FreshNetProduct  # Specify the model
        template_name = 'products/delete-product.html'
        success_url = reverse_lazy('all products')
        context_object_name = 'product'

@method_decorator(admin_group_required, name='dispatch')
class EditProductView(views.UpdateView):
    model = FreshNetProduct
    form_class = ProductBaseForm
    template_name = 'products/edit-product.html'
    context_object_name = 'product'

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if not request.user == product.user and not request.user.is_superuser:
            return render(request, '403.html', status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('product-details', kwargs={'pk': self.object.pk})

@method_decorator(admin_group_required, name='dispatch')
class DeleteProductView(views.DeleteView):
    model = FreshNetProduct
    template_name = 'products/delete-product.html'
    success_url = reverse_lazy('all products')
    context_object_name = 'product'