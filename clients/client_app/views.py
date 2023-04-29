from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm, OrderServiceForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import FormView
from worker_app.models import Worker
from administrator_app.models import Service, WorkDayAssignment
from .models import Order


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
    template_name = "client_app/logout.html"
    next_page = "/"


class MyProfileView(View):
    template_name = "client_app/my_profile.html"

    def get(self, request):
        active_order = Order.objects.filter(user=request.user, active=True)
        return render(request, self.template_name, {
            "active_order": active_order
        })


class MainPageView(View):
    template_name = "client_app/for_unreg_users.html"

    def get(self, request):
        return render(request, self.template_name)


class WorkerProfileView(View):
    template_name = "client_app/worker_info.html"

    def get(self, request, first_name):
        worker = Worker.objects.filter(first_name=first_name)
        return render(request, self.template_name, {"worker": worker})


class ServiceProfileView(View):
    template_name = "client_app/service.html"

    def get(self, request, name):
        service = Service.objects.filter(name=name)
        return render(request, self.template_name, {"service": service})


class OrderServiceView(View):
    template_name = "client_app/order_service.html"
    success_url = "order_service"

    def get(self, request):
        form = OrderServiceForm
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            service = form.cleaned_data.get("service")
            form.save(request.user)
            messages.success(request, f"You have ordered {service} successfully !!!")
            return redirect(self.success_url)
        return render(request, self.template_name, {"form": form})
