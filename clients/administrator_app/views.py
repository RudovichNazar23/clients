from django.shortcuts import render
from django.contrib.auth.views import LogoutView


class SignOutView(LogoutView):
    template_name = "administrator_app/main_admin.html"
    next_page = "/"
