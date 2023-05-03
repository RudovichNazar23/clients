import datetime

from django.shortcuts import render
from django.views import View
from administrator_app.models import Service, WorkDay, WorkDayAssignment
from administrator_app.forms import DeactivateOrderForm
from worker_app.models import Worker
from client_app.models import Order
import datetime


class Main(View):
    def get(self, request):
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

