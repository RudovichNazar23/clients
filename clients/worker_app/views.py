from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.views import View
"""from administrator_app.models import WorkSchedule"""


class SignOutView(LogoutView):
    template_name = "client_app/my_profile.html"
    next_page = "/"


