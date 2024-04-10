from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from bgfreshnet.events.decorators import admin_group_required
from bgfreshnet.events.forms import EventCreateForm, EventBaseForm
from bgfreshnet.events.models import Event
from django.views import generic as views

# Create your views here.
class AllEventsView(views.ListView):
    model = Event
    template_name = 'events/all-events.html'
    context_object_name = 'events'

@method_decorator(admin_group_required, name='dispatch')
class AddEventView(views.CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'events/add-event.html'
    success_url = reverse_lazy('all events')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DetailsEventView(views.DetailView):
    model = Event
    template_name = 'events/details-event.html'
    context_object_name = 'event'

class EditEventView(views.UpdateView):
    form_class = EventBaseForm
    template_name = 'events/edit-event.html'  # Update with your actual template name
    success_url = reverse_lazy('details event')