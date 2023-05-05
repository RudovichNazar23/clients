from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from administrator_app.models import Service, WorkDay, WorkDayAssignment
from administrator_app.forms import DeactivateOrderForm
from worker_app.models import Worker
from client_app.models import Order
import datetime


class Main(View):
    def get(self, request):
        self.check_dates()
        if request.user.is_superuser:
            workday = WorkDay.objects.filter(date=datetime.date.today())
            assignments = WorkDayAssignment.objects.filter(workday__id__in=workday)
            orders = Order.objects.filter(worker_and_date__id__in=assignments, active=True).order_by("time")
            form = DeactivateOrderForm()
            return render(request, "administrator_app/main_admin.html", {"current_orders": orders,
                                                                         "form": form})

        elif request.user.is_staff:
            workday = WorkDay.objects.filter(date=datetime.date.today())
            worker_assignments = WorkDayAssignment.objects.filter(worker=request.user.id, workday__id__in=workday)
            orders = Order.objects.filter(worker_and_date__id__in=worker_assignments, active=True).order_by("time")
            return render(request, "worker_app/main_worker.html", {"current_orders": orders})

        else:
            workers = Worker.objects.all()
            services = Service.objects.all()
            return render(request, "client_app/home.html", {
                "workers": workers,
                "services": services
            })

    def check_dates(self):
        current_date = datetime.date.today()
        for workday in WorkDay.objects.filter(active=True):
            if workday.date < current_date:
                workday.active = False
                workday.save()
            continue


class ClientProfileView(View):
    template_name = "main_app/client_profile.html"

    def get(self, request, first_name):
        client = User.objects.get(first_name=first_name)
        return render(request, self.template_name, {"client": client})
