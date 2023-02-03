from django import forms
from .models import Service, WorkSchedule
from django.core.exceptions import ValidationError


class CreateServiceForm(forms.Form):
    service_name = forms.CharField(
        label="Name of the service",
        required=True,
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
        service_name = self.cleaned_data.get("service_name")
        description = self.cleaned_data.get("description")
        price = self.cleaned_data.get("price")

        service = Service(
            service_name=service_name,
            description=description,
            price=price
        ).save()

        return service

    def clean_service_name(self):
        new_service_name = self.cleaned_data.get("service_name")

        if Service.objects.filter(service_name=new_service_name):
            raise ValidationError(
                "Service with this name already exists"
            )
        return new_service_name


class WorkScheduleForm(forms.ModelForm):
    date = forms.DateField(label="Date", required=True, widget=forms.SelectDateWidget())

    class Meta:
        model = WorkSchedule
        fields = ["worker", "time_from", "time_to"]

    def save_data(self):
        worker = self.cleaned_data.get("worker")
        date = self.cleaned_data.get("date")
        time_from = self.cleaned_data.get("time_from")
        time_to = self.cleaned_data.get("time_to")

        schedule = WorkSchedule(
            worker=worker,
            date=date,
            time_from=time_from,
            time_to=time_to
        ).save()

        return schedule


"""    
    def clean_time_to(self):
        time_from = self.cleaned_data.get("time_from")
        time_to = self.cleaned_data.get("time_to")

        if time_from == time_to:
            raise ValidationError(
                "No"
            )
        return time_to"""
