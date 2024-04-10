from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg

from bgfreshnet.freshnet_products.models import FreshNetProduct

# Create your models here.
UserModel = get_user_model()
class ProductComment(models.Model):
    MAX_LENGTH = 500

    text = models.TextField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    product = models.ForeignKey(
        FreshNetProduct,
        on_delete=models.DO_NOTHING,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class ProductRating(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        FreshNetProduct,
        on_delete=models.CASCADE,
    )

    rating = models.IntegerField(
        default=0,
    )
    def average_rating(self) -> float:
        return ProductRating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0