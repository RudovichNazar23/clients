from django.contrib import admin

from .models import Service, WorkDay, WorkDayAssignment, WorkTime, WorkTimeAssignment

admin.site.register(Service)
admin.site.register(WorkDay)
admin.site.register(WorkDayAssignment)
admin.site.register(WorkTime)
admin.site.register(WorkTimeAssignment)
