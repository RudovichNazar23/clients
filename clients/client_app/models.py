from django.db import models
from django.contrib.auth.models import User
from worker_app.models import Worker
from administrator_app.models import Service, WorkDayAssignment


class NotRegisteredUser(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=50, null=False, unique=True, error_messages={"unique": "Must be unique"})
    phone_number = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{self.first_name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    worker_and_date = models.ForeignKey(WorkDayAssignment, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    time = models.CharField(verbose_name="Time of service", max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user}"


class Feedback(models.Model):
    pass
