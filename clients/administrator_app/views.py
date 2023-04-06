from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LogoutView
from .forms import CreateServiceForm, CreateWorkDayForm, CreateAssignmentForm
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.edit import FormView
from worker_app.models import Worker
from .models import WorkDay
import datetime


class CreateServiceView(FormView):
    template_name = "administrator_app/create_service.html"
    form_class = CreateServiceForm
    success_url = "create_service"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateWorkDayView(FormView):
    template_name = "administrator_app/create_workday.html"
    form_class = CreateWorkDayForm
    success_url = "create_assignment"

    def get(self, request, *args, **kwargs):
        self.clean_dates()
        return render(request, self.template_name, {"form": self.form_class})

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def clean_dates(self):
        today = datetime.date.today()
        for date in WorkDay.objects.all():
            if date.date < today:
                WorkDay.objects.filter(date=str(date)).delete()


class CreateWorkdayAssignment(FormView):
    template_name = "administrator_app/create_assignment.html"
    form_class = CreateAssignmentForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class WorkerListView(ListView):
    template_name = "administrator_app/worker_list.html"
    model = Worker
    context_object_name = "workers"
    ordering = "id"


class WorkerProfileView(View):
    template_name = "administrator_app/worker_profile.html"

    def get(self, request, first_name):
        worker = Worker.objects.filter(first_name=first_name)
        return render(request, self.template_name, {"worker": worker})


class SignOutView(LogoutView):
    template_name = "administrator_app/main_admin.html"
    next_page = "/"
