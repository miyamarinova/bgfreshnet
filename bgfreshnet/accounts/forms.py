from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms, get_user_model

from bgfreshnet.accounts.models import FreshNetUser

UserModel = get_user_model()
class FreshNetUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = FreshNetUser
        fields = ('email', 'first_name', 'last_name', 'name_farm')
class FreshNetChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel



