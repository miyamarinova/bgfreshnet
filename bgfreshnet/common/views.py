from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as views

from bgfreshnet.accounts.models import Profile, FreshNetUser
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



