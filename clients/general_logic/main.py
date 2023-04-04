from django.shortcuts import render
from django.views import View


class Main(View):
    def get(self, request):
        if request.user.is_superuser:
            return render(request, "administrator_app/main_admin.html")
        elif request.user.is_staff:
            return render(request, "worker_app/main_worker.html")
        else:
            return render(request, "client_app/home.html")

