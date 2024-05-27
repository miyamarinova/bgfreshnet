from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from bgfreshnet.common.forms import ProductSearchForm
from bgfreshnet.common.models import ProductRating
from bgfreshnet.freshnet_products.decorators import admin_group_required, has_delete_permission
from bgfreshnet.freshnet_products.forms import ProductCreateForm, ProductBaseForm, ProductEditForm, RatingForm
from bgfreshnet.freshnet_products.models import FreshNetProduct
from django.utils.decorators import method_decorator

@login_required
def has_permission(user, product_id):
    try:
        product = FreshNetProduct.objects.get(pk=product_id)
        return product.user == user
    except FreshNetProduct.DoesNotExist:
        return False
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
    template_name = 'products/all-products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query', None)
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ProductSearchForm(self.request.GET or None)
        context['search_form'] = form
        return context

class ProductDetailsView(views.DetailView):
    model = FreshNetProduct
    template_name = 'products/product-details.html'  # Specify the template for product details
    context_object_name = 'product'  # Specify the context variable name to use in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        product = self.object

        # Get average rating
        context['average_rating'] = ProductRating.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg'] or 0
        context['rating_count'] = ProductRating.objects.filter(product=product).count()
        # Add the rating form
        context['form'] = RatingForm()

        if user.is_authenticated:
            # Check if the user has rated this product
            context['has_rated'] = ProductRating.objects.filter(user=user, product=product).exists()
        else:
            context['has_rated'] = False

        return context

class EditProductView(views.UpdateView):
    model = FreshNetProduct
    form_class = ProductEditForm
    template_name = 'products/edit-product.html'
    context_object_name = 'product'

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if not request.user == product.user:
            return render(request, '403.html', status=403)
        return super().dispatch(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('product-details', kwargs={'pk': self.object.pk})

class DeleteProductView(views.DeleteView):
    model = FreshNetProduct
    template_name = 'products/delete-product.html'
    success_url = reverse_lazy('all products')

    def dispatch(self, request, *args, **kwargs):
        # Get the product object
        product = self.get_object()
        # Check if the current user is the one who added the product
        if request.user != product.user:
            messages.error(request, 'You do not have permission to delete this product.')
            return redirect('product-details', pk=product.pk)
        return super().dispatch(request, *args, **kwargs)


@login_required
def rate_product(request, product_id):
    product = get_object_or_404(FreshNetProduct, id=product_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            ProductRating.objects.update_or_create(
                user=request.user,
                product=product,
                defaults={'rating': rating},
            )
            return redirect('product-details', pk=product.id)
    else:
        form = RatingForm()

    return render(request, 'products/product-details.html', {'form': form, 'product': product})