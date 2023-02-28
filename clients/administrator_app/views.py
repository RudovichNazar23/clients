from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import FormView
from .forms import CreateServiceForm, WorkScheduleForm


class CreateServiceView(FormView):
    template_name = "administrator_app/create_service.html"
    form_class = CreateServiceForm
    success_url = "create_service"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateWorkScheduleView(FormView):
    template_name = "administrator_app/create_schedule.html"
    form_class = WorkScheduleForm
    success_url = "/"

    def form_valid(self, form):
        form.save_data()
        form.create_time_range()
        return super().form_valid(form)


class SignOutView(LogoutView):
    template_name = "administrator_app/main_admin.html"
    next_page = "/"
