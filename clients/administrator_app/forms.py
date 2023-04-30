from django import forms

from .models import Service, WorkDay, WorkDayAssignment
from client_app.models import Order
from django.core.exceptions import ValidationError
import datetime


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
            name=service_name,
            description=description,
            price=price
        ).save()

        return service

    def clean_service_name(self):
        new_service_name = self.cleaned_data.get("service_name")

        if Service.objects.filter(name=new_service_name):
            raise ValidationError(
                "Service with this name already exists"
            )
        return new_service_name


class CreateWorkDayForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "special"}))

    def save(self):
        date = self.cleaned_data.get("date")
        workday = WorkDay(
            date=date
        )

        return workday.save()

    def clean_date(self):
        date = self.cleaned_data.get("date")
        if WorkDay.objects.filter(date=date):
            raise ValidationError(
                "This date already exists"
            )
        elif date <= datetime.date.today():
            raise ValidationError(
                "The selected workday is in the past. Please choose the future date"
            )
        return date


class CreateAssignmentForm(forms.ModelForm):
    class Meta:
        model = WorkDayAssignment
        fields = ("workday", "worker")
        widgets = {
            "workday": forms.Select(choices=[(i, i) for i in WorkDay.objects.all() if i.date > datetime.date.today()])
        }

    def save(self, commit=True):
        workday = self.cleaned_data.get("workday")
        worker = self.cleaned_data.get("worker")

        assignment = WorkDayAssignment(
            workday=workday,
            worker=worker
        )

        return assignment.save()

    def clean(self):
        worker = self.cleaned_data.get("worker")
        workday = self.cleaned_data.get("workday")

        assignment = WorkDayAssignment.objects.filter(worker=worker, workday=workday).exists()
        if assignment:
            self.add_error("worker", f"Workday for {worker} already exists")


class DeactivateServiceForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("active",)
        widgets = {
            forms.CheckboxInput()
        }

