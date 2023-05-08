import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LogoutView
from .forms import CreateServiceForm, CreateWorkDayForm, CreateAssignmentForm,\
    DeactivateOrderForm, CreateWorkTimeForm, CreateWorkTimeAssignmentForm
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.edit import FormView
from worker_app.models import Worker
from client_app.models import Order
from .models import WorkDay, WorkDayAssignment


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
        return render(request, self.template_name, {"form": self.form_class})

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateWorkdayAssignment(FormView):
    template_name = "administrator_app/create_assignment.html"
    form_class = CreateAssignmentForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateWorkTimeView(FormView):
    template_name = "administrator_app/create_worktime.html"
    form_class = CreateWorkTimeForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateWorkTimeAssignmentView(FormView):
    template_name = "administrator_app/create_time_assignment.html"
    form_class = CreateWorkTimeAssignmentForm
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
        workday = WorkDay.objects.filter(date=datetime.date.today())
        worker_assignments = WorkDayAssignment.objects.filter(worker__id__in=worker, workday__id__in=workday)
        current_orders = Order.objects.filter(worker_and_date__id__in=worker_assignments, active=True)
        return render(request, self.template_name, {"worker": worker,
                                                    "worker_assignments": worker_assignments,
                                                    "current_orders": current_orders
                                                    }
                      )


class WorkerScheduleView(View):
    template_name = "administrator_app/worker_schedule.html"

    def get(self, request, first_name):
        worker = Worker.objects.get(first_name=first_name)
        assignments = WorkDayAssignment.objects.filter(worker=worker.id)
        return render(request, self.template_name, {"assignments": assignments})


class SignOutView(LogoutView):
    template_name = "administrator_app/main_admin.html"
    next_page = "/"


class DeactivateOrderView(View):
    def post(self, request, id: int):
        order = Order.objects.get(id=id)
        form = DeactivateOrderForm(request.POST)
        if form.is_valid():
            order.active = False
            order.save()
            return redirect("/")
        return redirect("create_workday")
