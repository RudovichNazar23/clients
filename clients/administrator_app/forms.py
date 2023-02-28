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
    date = forms.DateField(label="Date", required=True, widget=forms.SelectDateWidget(attrs={"class": "special"}))

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

    def create_time_range(self):
        time_from = self.cleaned_data.get("time_from")
        time_to = self.cleaned_data.get("time_to")

        for elem in WorkSchedule.TIME_CHOICES:
            for time1 in elem:
                time1 = time_from
                if time1 == elem[0]:
                    time_from = elem
                    ind1 = WorkSchedule.TIME_CHOICES.index(time_from)

            for time2 in elem:
                time2 = time_to
                if time2 == elem[0]:
                    time_to = elem
                    ind2 = WorkSchedule.TIME_CHOICES.index(time_to)
        WorkSchedule.TIME_CHOICES = WorkSchedule.TIME_CHOICES[ind1:ind2]
        return WorkSchedule.TIME_CHOICES

    def clean_time_to(self):
        time_from = self.cleaned_data.get("time_from")
        time_to = self.cleaned_data.get("time_to")

        if time_from == time_to:
            raise ValidationError(
                f"You cannot create schedule like this: {time_from} - {time_to}"
            )
        elif int(time_to[:time_to.find(":")]) < int(time_from[:time_from.find(":")]):
            raise ValidationError(
                f"{time_from} - {time_to} is invalid period"
            )
        elif int(time_to[:time_to.find(":")]) == int(time_from[:time_from.find(":")]):
            if int(time_to[time_to.find(":") + 1:]) < int(time_from[time_from.find(":") + 1:]):
                raise ValidationError(
                    f"{time_from} - {time_to} is invalid period"
                )
        return time_to

    def clean_date(self):
        worker = self.cleaned_data.get("worker")
        date = self.cleaned_data.get("date")

        if WorkSchedule.objects.filter(worker=worker, date=date):
            raise ValidationError(
                f"This schedule for {worker} on this day already exists"
            )
        return date
