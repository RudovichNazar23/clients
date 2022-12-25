from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class RegistrationForm(forms.Form):
    username = forms.EmailField(error_messages={"required": "Wrong data"}, label="Your email", required=True)
    first_name = forms.CharField(error_messages={"errors": "Wrong data"}, required=True)
    last_name = forms.CharField(error_messages={"errors": "Wrong data"}, required=True)
    password = forms.CharField(error_messages={"errors": "Wrong data"}, widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), min_length=8,)

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get("username"),
            first_name=self.cleaned_data.get("first_name"),
            last_name=self.cleaned_data.get("last_name"),
            password=self.cleaned_data.get("password")
        )
        return user
