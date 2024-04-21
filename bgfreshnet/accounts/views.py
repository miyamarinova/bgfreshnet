from urllib import request
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from bgfreshnet.accounts.forms import FreshNetUserCreationForm, FreshNetChangeForm
from bgfreshnet.accounts.models import Profile
from bgfreshnet.freshnet_products.models import FreshNetProduct

UserModel = get_user_model()

class LogInUserView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'

class FreshNetUserRegistrationView(views.CreateView):
    template_name = 'accounts/register_user.html'
    form_class = FreshNetUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result

def logout_user(request):
        logout(request)
        return redirect('index')

@login_required
def vendor_admin(request):
    vendor = UserModel
    products = FreshNetProduct.objects.all()

    return render(request, 'common/index.html',
                  {'vendor': vendor, 'products':products})


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/details_profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        # Fetch all products associated with this profile's user
        products = FreshNetProduct.objects.filter(user=profile.user)
        context['products'] = products
        return context

class ProfileUpdateView(views.UpdateView):
    model = Profile
    template_name = 'accounts/edit_user.html'
    fields = ['profile_picture', 'short_bio', 'phone_number']  # Fields to be updated

    def get_object(self, queryset=None):
        # Retrieve the profile object for the logged-in user
        return self.request.user.profile

    def form_valid(self, form):
        # Ensure the user associated with the profile is the logged-in user
        if form.instance.user != self.request.user:
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk
        })
class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/delete_profile.html'  # Your delete confirmation template
    success_url = reverse_lazy('list producers')  # URL to redirect after successful deletion
    context_object_name = 'profile'  # The name of the variable to use in the template context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.object.user
        self.object.delete()  # Delete the profile
        user.delete()  # Delete the associated user
        return HttpResponseRedirect(self.get_success_url())