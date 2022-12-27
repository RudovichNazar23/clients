from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
class RegistrationForm(forms.Form):
    username = forms.EmailField(
        label="Your email",
        required=True
    )
    first_name = forms.CharField(
        required=True
    )
    last_name = forms.CharField(
        required=True
    )
    password1 = forms.CharField(
        label="Password" ,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        min_length=8,
    )
    password2 = forms.CharField(
        required=True,
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"})
    )

    def clean_username(self):
        new_user = self.cleaned_data.get("username")
        if User.objects.filter(username=new_user):
            raise ValidationError(
                "This user already exists"
            )
        return new_user

    def clean_first_last_name(self):
        pass

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get("username"),
            first_name=self.cleaned_data.get("first_name"),
            last_name=self.cleaned_data.get("last_name"),
            password=self.cleaned_data.get("password")
        )
        return user
