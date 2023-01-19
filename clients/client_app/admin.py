from django.contrib import admin
from .models import NotRegisteredUser, Order, Feedback

admin.site.register(NotRegisteredUser)
admin.site.register(Order)
admin.site.register(Feedback)


