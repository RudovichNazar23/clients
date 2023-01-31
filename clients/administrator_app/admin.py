from django.contrib import admin

from .models import Service, WorkSchedule

admin.site.register(Service)
admin.site.register(WorkSchedule)