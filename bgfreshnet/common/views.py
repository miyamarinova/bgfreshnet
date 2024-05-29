from django.conf import settings
import logging
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import generic as views
from bgfreshnet.accounts.models import Profile, FreshNetUser
from bgfreshnet.common.forms import ContactForm, CommentForm, ProductSearchForm
from bgfreshnet.events.models import Event
from bgfreshnet.freshnet_products.models import FreshNetProduct
from django.core.mail import send_mail

logger = logging.getLogger(__name__)
# Create your views here.

UserModel = get_user_model()
template_name = 'common/index.html'

class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.prefetch_related("user").all()
        context['events'] = Event.objects.all()  # Add this line to fetch events data
        return context
    def get(self, request, *args, **kwargs):
        form = ProductSearchForm(request.GET or None)
        products = FreshNetProduct.objects.all()

        if form.is_valid():
            query = form.cleaned_data['query']
            products = products.filter(name__icontains=query)

        context = {
            'profiles': Profile.objects.prefetch_related("user").all(),
            'events': Event.objects.all(),
            'form': form,
            'products': products,
        }
        return render(request, self.template_name, context)

class AboutUsView(views.TemplateView):
    template_name = "common/about-us.html"

def search_product(request):
    form = ProductSearchForm()
    products = None

    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = FreshNetProduct.objects.filter(name__icontains=query)

    return render(request, 'common/search-result.html', {'form': form, 'products': products})

def contact(request):
    email_sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email notification to your email address
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=f"You have received a new message from {name} ({email}): \n\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
            )
            email_sent=True
            return render(request, 'common/thanks.html')
    else:
        form = ContactForm()

    return render(request, 'common/contact-us.html', {'form': form, 'email_sent':email_sent})

def custom_403_forbidden(request, exception):
    return render(request, 'common/403_forbidden.html', status=403)

def like_product(request, product_id):
    product = FreshNetProduct.objects.get(id=product_id)
    liked_object = FreshNetProduct.objects.filter(to_product_id=product_id, user=request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        like = FreshNetProduct(to_product=product, user=request.user)
        like.save()
    return redirect(request.META['HTTP_REFERER'] + f'#{product_id}')

def comment_product(request, product_id):
    if request.method == 'POST':
        product = FreshNetProduct.objects.get(id=product_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_product = product
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{product_id}')