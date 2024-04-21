from django.contrib.auth import get_user_model
from django.core.mail import send_mail, BadHeaderError, EmailMessage, get_connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from bgfreshnet import settings
from bgfreshnet.accounts.models import Profile, FreshNetUser
from bgfreshnet.common.forms import ContactForm
from bgfreshnet.events.models import Event

# Create your views here.

UserModel = get_user_model()
class IndexView(views.TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.prefetch_related("user").all()
        context['events'] = Event.objects.all()  # Add this line to fetch events data
        return context
class AboutUsView(views.TemplateView):
    template_name = "common/about-us.html"

class AllProducersView(views.ListView):
    model = FreshNetUser
    template_name = 'accounts/producer_list.html'
    context_object_name = 'producers'

    def get_queryset(self):
        # Exclude the superuser from the list of producers
        return FreshNetUser.objects.exclude(is_superuser=True)


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