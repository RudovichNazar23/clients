from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView


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


class LoginView(View):
    template_name = "client_app/login.html"
    success_url = "/"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(self.success_url)
            else:
                messages.error(request, "You have wrong email or password, please try again...")
                return render(request, self.template_name, {"form": form})


class SignOutView(LogoutView):
    template_name = "client_app/my_profile.html"
    next_page = "/"


class MyProfileView(View):
    template_name = "client_app/my_profile.html"

    def get(self, request):
        return render(request, self.template_name)


class MainPageView(View):
    template_name = "client_app/for_unreg_users.html"

    def get(self, request):
        return render(request, self.template_name)
