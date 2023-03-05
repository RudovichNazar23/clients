from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.views import View
from administrator_app.models import WorkSchedule


class SignOutView(LogoutView):
    template_name = "client_app/my_profile.html"
    next_page = "/"


class MyScheduleView(View):
    template_name = "worker_app/schedule.html"

    def get(self, request):
        dates = WorkSchedule.objects.filter(worker=request.user)
        return render(request, self.template_name, {"dates": dates})


class WorkTimeOnDateView(View):
    template_name = "worker_app/time_on_date.html"

    def get(self, request, date):
        time = WorkSchedule.objects.filter(date=date)
        return render(request, self.template_name, {"time": time,
                                                    }
                      )
