import datetime

from django.shortcuts import render
from django.views import View
from administrator_app.models import Service, WorkDay, WorkDayAssignment
from worker_app.models import Worker
from client_app.models import Order
import datetime


class Main(View):
    def get(self, request):
        if request.user.is_superuser:
            return render(request, "administrator_app/main_admin.html")
        elif request.user.is_staff:
            workday = WorkDay.objects.filter(date=datetime.date.today())
            worker_assignments = WorkDayAssignment.objects.filter(worker=request.user.id, workday__id__in=workday)
            orders = Order.objects.filter(worker_and_date__id__in=worker_assignments).order_by("time")
            return render(request, "worker_app/main_worker.html", {"current_orders": orders})
        else:
            workers = Worker.objects.all()
            services = Service.objects.all()
            return render(request, "client_app/home.html", {
                "workers": workers,
                "services": services
            })

