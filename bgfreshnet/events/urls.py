from django.urls import path

from bgfreshnet.events.views import AllEventsView, AddEventView, DetailsEventView, EditEventView

urlpatterns=[
    path('all-events/', AllEventsView.as_view(), name='all events'),
    path('add-event/', AddEventView.as_view(), name='add event'),
    path('details-event/<int:pk>', DetailsEventView.as_view(), name='details event'),
    path('edit-event/<int:pk>/', EditEventView.as_view(), name='edit event')
]