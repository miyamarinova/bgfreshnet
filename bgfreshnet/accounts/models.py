from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from bgfreshnet.accounts.managers import FreshNetUserManager

MAX_FIRST_NAME_LENGTH = 30
MAX_LAST_NAME_LENGTH = 30

class FreshNetUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _("email"),
        unique=True,
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=False,
        null=False,
    )

    name_farm = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=False,
        null=False,
    )


    date_jointed = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = FreshNetUserManager()


# Create your models here.
class Profile(models.Model):

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    short_bio = models.TextField(
        blank=True,
        null=True,
        help_text='Short description of you and your products.'
    )
    phone_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        FreshNetUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def delete(self, *args, **kwargs):
        # Delete related products
        self.user.products.all().delete()
        # Delete the user
        self.user.delete()
        # Call the superclass delete method to delete the profile
        super().delete(*args, **kwargs)


