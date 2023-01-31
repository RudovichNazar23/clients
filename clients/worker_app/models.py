from django.db import models
from django.contrib.auth.models import User


class Worker(User):
    pass

    def __str__(self):
        return f"{self.first_name}"
