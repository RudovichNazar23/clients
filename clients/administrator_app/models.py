from django.db import models
from worker_app.models import Worker
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.service_name}"


@deconstructible
class WorkTime:
    __TIME_FORMAT = "hours:minutes"

    def __init__(self, time, *args, **kwargs):
        super().__init__()
        self.time = time
        self._ordered = False

    @property
    def ordered(self):
        return self._ordered

    @ordered.setter
    def ordered(self):
        self._ordered = True


class WorkSchedule(models.Model):
    TIME_CHOICES = (
        ("8:00", WorkTime("8:00").time),
        ("8:45", WorkTime("8:45").time),
        ("9:30", WorkTime("9:30").time),
        ("10:15", WorkTime("10:15").time),
        ("11:00", WorkTime("11:00").time),
        ("11:45", WorkTime("11:45").time),
        ("12:30", WorkTime("12:30").time),
        ("13:15", WorkTime("13:15").time),
        ("14:00", WorkTime("14:00").time),
        ("14:45", WorkTime("14:45").time),
        ("15:30", WorkTime("15:30").time),
        ("16:15", WorkTime("16:15").time),
        ("17:00", WorkTime("17:00").time),
        ("17:30", WorkTime("17:30").time)
    )
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    time_from = models.CharField(choices=TIME_CHOICES, max_length=100)
    time_to = models.CharField(choices=TIME_CHOICES, max_length=100)

    def __str__(self):
        return f"{self.worker} : {self.date}"
