from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()
# Create your models here.
class Event(models.Model):
    event_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )

    organiser_of_event = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    date_of_event = models.DateTimeField(
        auto_now_add=False,
        null=False,
        blank=False,
    )

    registration_fees = models.IntegerField(
        default=0,
        help_text="Enter Registration Fees For The Event in Rupees",
    )

    details = models.TextField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    event_image = models.ImageField(
        upload_to="events",
    )
