from django import forms
from .models import Service
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class CreateServiceForm(forms.Form):
    service_name = forms.CharField(
        label="Name of the service",
        required=True
    )

    description = forms.CharField(
        label="Description",
        required=True,
        widget=forms.Textarea()
    )

    price = forms.IntegerField(
        label="Price",
        required=True,
    )

    def save(self):
        service = Service(
            service_name=self.cleaned_data.get("service_name"),
            description=self.cleaned_data.get("description"),
            price=self.cleaned_data.get("price")
        ).save()
        return service

    def clean_service_name(self):
        service_name = self.cleaned_data.get("service_name")
        if Service.objects.filter(service_name=service_name):
            raise ValidationError(
                "This service already exists"
            )
        return service_name

