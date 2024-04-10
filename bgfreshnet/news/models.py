from django.db import models

# Create your models here.
class Article(models.Model):

    MAX_LENGTH_TITLE = 150

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        blank=False,
        null=False,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    content = models.TextField(
        blank=False,
        null=False,
    )

    # TO DO: Change this to ImageField
    article_image = models.URLField(
        blank=True,
        null=True,
    )

