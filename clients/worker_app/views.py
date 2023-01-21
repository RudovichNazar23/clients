from django.shortcuts import render
from django.contrib.auth.views import LogoutView


class SignOutView(LogoutView):
    template_name = "client_app/my_profile.html"
    next_page = "/"

