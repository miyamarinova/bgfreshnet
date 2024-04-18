from django.contrib.auth import get_user_model
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

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
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            send_mail('The contact form subject',
                      'This is the message', 'miyamarinova@gmail.com',
                      [email])

            return redirect('thanks')
    else:
        form = ContactForm()

    return render(request, 'common/contact-us.html', {'form': form})


def thanks(request):
    return render(request, 'common/thanks.html', )