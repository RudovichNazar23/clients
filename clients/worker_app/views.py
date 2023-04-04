from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.views import View
from administrator_app.models import WorkDayAssignment


class SignOutView(LogoutView):
    template_name = "client_app/my_profile.html"
    next_page = "/"


class MyScheduleView(View):
    template_name = "worker_app/schedule.html"

    def get(self, request):
        assignments = WorkDayAssignment.objects.filter(worker=request.user.id)
        return render(request, self.template_name, {"assignments": assignments})
