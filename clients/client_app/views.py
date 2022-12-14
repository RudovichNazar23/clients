from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

class RegistrationView(View):
    template_name = "client_app/registration.html"
    def get(self, request):
        context = {
            "form": RegistrationForm()
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = RegistrationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            return render(request, self.template_name, context)

class MyProfileView(View):
    template_name = "client_app/my_profile.html"
    def get(self, request):
        return render(request, self.template_name)
