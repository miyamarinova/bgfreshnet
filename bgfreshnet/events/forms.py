from django import forms
from bgfreshnet.events.models import Event

class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'organised_by', 'date_of_event', 'registration_fee', 'details', 'event_image','location']

        widgets = {
            "event_name": forms.TextInput(attrs={"placeholder": "Какво е това"}),
            "organised_by": forms.TextInput(attrs={"placeholder": "Кой го организира"}),
            "date_of_event": forms.DateInput(attrs={"placeholder": "Кога "}),
            "details": forms.Textarea(attrs={"placeholder": "Описание на събитието "}),
            "location": forms.TextInput(attrs={"placeholder": "Къде"}),

        }
        labels = {
            "event_name": "Име на събитието",
            "organised_by": "Организатор",
        }

class EventCreateForm(EventBaseForm):
    pass