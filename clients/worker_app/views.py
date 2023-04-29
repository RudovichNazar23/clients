from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.views import View
from administrator_app.models import WorkDayAssignment
from client_app.models import Order


class SignOutView(LogoutView):
    template_name = "client_app/my_profile.html"
    next_page = "/"


class MyScheduleView(View):
    template_name = "worker_app/schedule.html"

    def get(self, request):
        assignments = WorkDayAssignment.objects.filter(worker=request.user.id).order_by("-workday_id")
        return render(request, self.template_name, {"assignments": assignments})


class DateOrdersView(View):
    template_name = "worker_app/orders.html"

    def get(self, request, id: int):
        assignment = WorkDayAssignment.objects.filter(worker=request.user.id, workday=id)
        orders = Order.objects.filter(worker_and_date__id__in=assignment).order_by("time")
        return render(request, self.template_name, {"orders": orders})
