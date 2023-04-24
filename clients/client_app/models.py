from django.db import models
from django.contrib.auth.models import User
from worker_app.models import Worker
from administrator_app.models import Service, WorkDayAssignment
from django.utils.deconstruct import deconstructible


class NotRegisteredUser(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=50, null=False, unique=True, error_messages={"unique": "Must be unique"})
    phone_number = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{self.first_name}"

@deconstructible
class Time(models.Model):
    def __init__(self, time: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time = time

    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.time}"


TIME_CHOICES = [
    ("9:00", Time("9:00")),
    ("9:45", Time("9:45")),
    ("10:30", Time("10:30")),
    ("11:15", Time("11:15")),
    ("12:00", Time("12:00")),
    ("12:45", Time("12:45")),
    ("13:30", Time("13:30")),
    ("14:15", Time("14:15")),
    ("15:00", Time("15:00")),
    ("15:45", Time("15:45")),
    ("16:30", Time("16:30")),
]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    worker_and_date = models.ForeignKey(WorkDayAssignment, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    time = models.CharField(verbose_name="Time of service", max_length=100, choices=TIME_CHOICES)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user}"


class Feedback(models.Model):
    pass
