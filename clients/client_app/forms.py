import datetime

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Order, Feedback
from administrator_app.models import WorkTime


class RegistrationForm(forms.Form):
    username = forms.EmailField(
        label="Your email",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "form-control"}),
        min_length=8,
    )
    password2 = forms.CharField(
        required=True,
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "form-control"})
    )

    def clean_username(self):
        new_user = self.cleaned_data.get("username")
        if User.objects.filter(username=new_user):
            raise ValidationError(
                "This user already exists"
            )
        return new_user

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "The two password fields didn’t match."
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get("username"),
            first_name=self.cleaned_data.get("first_name"),
            last_name=self.cleaned_data.get("last_name"),
            password=self.cleaned_data.get("password1")
        )
        return user


class LoginForm(forms.Form):
    username = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}
                                   )
    )


class OrderServiceForm(forms.ModelForm):
    def __init__(self, worktime, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["time"] = forms.ModelChoiceField(queryset=worktime)

    class Meta:
        model = Order
        fields = ("service", "time")
        widgets = {
            "time": forms.Select()
        }

    def save(self, user, worker_and_date, commit=True):
        service = self.cleaned_data.get("service")
        time = self.cleaned_data.get("time")

        order = Order(
            user=user,
            worker_and_date=worker_and_date,
            service=service,
            time=time
        )
        time.ordered = True
        time.save()
        return order.save()


class LeaveFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("description",)

    def save(self, user, order, commit=True):
        description = self.cleaned_data.get("description")

        feedback = Feedback(
            user=user,
            order=order,
            description=description
        )
        order.has_feedback = True
        order.save()
        return feedback.save()


