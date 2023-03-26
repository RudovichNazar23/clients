from django.contrib import admin

from .models import Service, WorkDay, WorkDayAssignment

admin.site.register(Service)
admin.site.register(WorkDay)
admin.site.register(WorkDayAssignment)
