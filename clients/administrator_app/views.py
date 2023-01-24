from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.views.generic import View
from django.views.generic.edit import FormView
from .forms import CreateServiceForm
from django.shortcuts import render
from django.contrib.auth.views import LogoutView


class CreateServiceView(View):
    template_name = "administrator_app/create_service.html"

    def get(self, request):
        form = CreateServiceForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CreateServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, self.template_name, {"form": form})


class SignOutView(LogoutView):
    template_name = "administrator_app/main_admin.html"
    next_page = "/"
