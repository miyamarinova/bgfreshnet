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

    organised_by = models.TextField(
        null=False,
        blank=False,
    )

    date_of_event = models.DateTimeField(
        auto_now_add=False,
        null=False,
        blank=False,
    )

    registration_fee = models.FloatField(
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

    event_image = models.URLField(
        blank=True,
        null=True,
    )

    location = models.TextField(
        blank=False,
        null=False,
    )