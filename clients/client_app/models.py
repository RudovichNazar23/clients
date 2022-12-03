from django.db import models
from django.contrib.auth.models import User
from worker_app.models import Worker
from administrator_app.models import Service
class Not_registered_user(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=50, null=False, unique=True)
    phone_number = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{self.first_name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="Worker")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="date_of_service")
    time = models.TimeField(verbose_name="time_of_service")

    def __str__(self):
        return f"{self.user}"


class Feedback(models.Model):
    pass