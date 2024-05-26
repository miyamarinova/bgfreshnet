from django.contrib.auth import get_user_model
from django.core.mail import send_mail, BadHeaderError, EmailMessage, get_connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from bgfreshnet import settings
from bgfreshnet.accounts.models import Profile, FreshNetUser
from bgfreshnet.common.forms import ContactForm, CommentForm, ProductSearchForm
from bgfreshnet.events.models import Event
from bgfreshnet.freshnet_products.models import FreshNetProduct

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
    if request.method == "POST":
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("email"), ]
            message = request.POST.get("message")
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

    return render(request, 'common/contact-us.html')

def thanks(request):
    return render(request, 'common/thanks.html', )


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