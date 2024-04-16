from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from bgfreshnet.accounts.models import FreshNetUser

UserModel = get_user_model()
class FreshNetUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = FreshNetUser
        fields = ('email', 'first_name', 'last_name', 'name_farm')

        labels = {
            "email": "Email",
            "first_name": "Собствено име",
            "last_name": "Фамилно име",
            "name_farm": "Име на ферма/фирма"
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].label = _("Парола")
            self.fields['password2'].label = _("Повтори парола")
class FreshNetChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel



