from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg


# Create your models here.
UserModel = get_user_model()

class FreshNetProduct(models.Model):
    MAX_NAME_LENGTH = 50

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False,
    )
    # TO DO: change this to ImageField

    product_image = models.URLField(
        null=False,
        blank=False,
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    date_added = models.DateField(auto_now_add=True)







