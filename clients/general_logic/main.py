from django.shortcuts import render
from django.views import View
from administrator_app.models import Service, WorkDay
from worker_app.models import Worker


class Main(View):
    def get(self, request):
        if request.user.is_superuser:
            return render(request, "administrator_app/main_admin.html")
        elif request.user.is_staff:
            return render(request, "worker_app/main_worker.html")
        else:
            workers = Worker.objects.all()
            services = Service.objects.all()
            return render(request, "client_app/home.html", {
                "workers": workers,
                "services": services
            })

