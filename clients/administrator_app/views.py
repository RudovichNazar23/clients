from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import FormView
from .forms import CreateServiceForm
from django.views.generic.list import ListView
from django.views import View
from worker_app.models import Worker


class CreateServiceView(FormView):
    template_name = "administrator_app/create_service.html"
    form_class = CreateServiceForm
    success_url = "create_service"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)





class WorkerListView(ListView):
    template_name = "administrator_app/worker_list.html"
    model = Worker
    context_object_name = "workers"


class WorkerProfileView(View):
    template_name = "administrator_app/worker_profile.html"

    def get(self, request, first_name):
        worker = Worker.objects.filter(first_name=first_name)
        return render(request, self.template_name, {"worker": worker})


class SignOutView(LogoutView):
    template_name = "administrator_app/main_admin.html"
    next_page = "/"
