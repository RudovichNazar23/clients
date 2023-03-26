from django import forms
from .models import Service, WorkDay, WorkDayAssignment
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


class CreateWorkDayForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "special"}))

    def save(self):
        date = self.cleaned_data.get("date")
        workday = WorkDay(
            date=date
        )

        return workday.save()


class CreateAssignmentForm(forms.ModelForm):
    class Meta:
        model = WorkDayAssignment
        fields = ("workday", "worker")

    def save(self, commit=True):
        workday = self.cleaned_data.get("workday")
        worker = self.cleaned_data.get("worker")

        assignment = WorkDayAssignment(
            workday=workday,
            worker=worker
        )

        return assignment.save()

