from django.contrib.auth import get_user_model
from django.core.validators import BaseValidator
from django.db import models
from django.utils.text import slugify
from bgfreshnet.accounts.models import FreshNetUser, Profile

SIZE_10_MB = 10 * 1024 * 1024

class MaxFileSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size
    def compare(self, file_size, max_size):
        return max_size < file_size

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

    product_image = models.ImageField(
        upload_to='product_photos/',
        validators=[
            MaxFileSizeValidator(limit_value=SIZE_10_MB)
        ],
        null=True,
        blank=True,
    )

    thumbnail = models.ImageField(
        upload_to='uploads/',
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    date_added = models.DateField(auto_now_add=True)

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')
        super().save(*args, **kwargs)

    user = models.ForeignKey(
        FreshNetUser,
        on_delete=models.RESTRICT,
        related_name='products'
    )

    def __str__(self):
        return self.name





