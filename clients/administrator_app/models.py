from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.service_name}"
