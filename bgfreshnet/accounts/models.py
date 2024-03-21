from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from bgfreshnet.accounts.managers import FreshNetUserManager
class FreshNetUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    PRODUCER = 1
    CONSUMER = 2

    ROLE_CHOICES = (
        (PRODUCER, "Producer Account"),
        (CONSUMER, "Consumer Account")
    )

    email = models.EmailField(
        _("email"),
        unique=True,
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    date_jointed = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )

    #role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    USERNAME_FIELD = "email"
    objects = FreshNetUserManager()


# Create your models here.
class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

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

    profile_picture = models.ImageField(
        blank=True,
        null=True
    )

    user = models.OneToOneField(
        FreshNetUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )



