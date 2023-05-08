from django.db import models
from worker_app.models import Worker
from django.utils.deconstruct import deconstructible


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class WorkDay(models.Model):
    date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date}"


class WorkDayAssignment(models.Model):
    workday = models.ForeignKey(WorkDay, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.worker} - {self.workday}"


class WorkTime(models.Model):
    time = models.TimeField(null=True)

    def __str__(self):
        return f"{self.time}"


class WorkTimeAssignment(models.Model):
    worktime = models.ForeignKey(WorkTime, on_delete=models.CASCADE)
    worker_assignment = models.ForeignKey(WorkDayAssignment, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.worktime}"

