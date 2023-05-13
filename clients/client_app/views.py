from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm, OrderServiceForm, LeaveFeedbackForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.views.generic.list import ListView
from worker_app.models import Worker
from administrator_app.models import Service, WorkDayAssignment, WorkTimeAssignment
from .models import Order, Feedback


class RegistrationView(View):
    template_name = "client_app/registration.html"

    def get(self, request):
        context = {
            "form": RegistrationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            return render(request, self.template_name, context)


class LoginView(View):
    template_name = "client_app/login.html"
    success_url = "/"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(self.success_url)
            else:
                messages.error(request, "You have wrong email or password, please try again...")
                return render(request, self.template_name, {"form": form})


class SignOutView(LogoutView):
    template_name = "client_app/logout.html"
    next_page = "/"


class MyProfileView(View):
    template_name = "client_app/my_profile.html"

    def get(self, request):
        active_order = Order.objects.filter(user=request.user, active=True)
        return render(request, self.template_name, {
            "active_order": active_order
        })


class WorkerProfileView(View):
    template_name = "client_app/worker_info.html"

    def get(self, request, first_name):
        worker = Worker.objects.filter(first_name=first_name)
        return render(request, self.template_name, {"worker": worker})


class WorkerFeedbacksView(View):
    template_name = "client_app/worker_feedbacks.html"

    def get(self, request, first_name):
        worker = Worker.objects.filter(first_name=first_name)
        worker_assignments = WorkDayAssignment.objects.filter(worker__id__in=worker)
        worker_orders = Order.objects.filter(worker_and_date__id__in=worker_assignments)
        feedbacks = Feedback.objects.filter(order__id__in=worker_orders)
        return render(request, self.template_name, {"feedbacks": feedbacks,
                                                    "worker": worker})


class ServiceProfileView(View):
    template_name = "client_app/service.html"

    def get(self, request, name):
        service = Service.objects.filter(name=name)
        return render(request, self.template_name, {"service": service})


class ChooseWorkerView(ListView):
    template_name = "client_app/choose_worker.html"
    model = Worker
    context_object_name = "workers"


class ChooseWorkerWorkDay(View):
    template_name = "client_app/choose_workday.html"

    def get(self, request, first_name: str):
        worker = get_object_or_404(Worker, first_name=first_name)
        worker_dates = WorkDayAssignment.objects.filter(worker=worker)
        return render(request, self.template_name, {"dates": worker_dates})


class OrderServiceView(View):
    template_name = "client_app/order_service.html"
    success_url = "/"

    def get(self, request, id: int):
        worker_assignment = WorkDayAssignment.objects.filter(id=id)
        worktime = WorkTimeAssignment.objects.filter(worker_assignment__id__in=worker_assignment, ordered=False)
        form = OrderServiceForm(worktime=worktime)
        return render(request, self.template_name, {"worktime": worktime,
                                                    "form": form
                                                    })

    def post(self, request, id):
        worker_assignment = WorkDayAssignment.objects.get(id=id)
        worktime = WorkTimeAssignment.objects.filter(worker_assignment=worker_assignment, ordered=False)
        form = OrderServiceForm(worktime, request.POST)
        if form.is_valid():
            form.save(
                user=request.user,
                worker_and_date=worker_assignment,

            )
            return redirect(self.success_url)


class MyVisitsView(View):
    template_name = "client_app/my_visits.html"

    def get(self, request):
        orders = Order.objects.filter(user=request.user, active=False).order_by("-worker_and_date")
        return render(request, self.template_name, {"orders": orders})


class LeaveFeedBackView(View):
    template_name = "client_app/leave_feedback.html"
    success_url = "/"

    def get(self, request, id):
        order = Order.objects.get(id=id)
        form = LeaveFeedbackForm()
        return render(request, self.template_name, {"form": form,
                                                    "order": order
                                                    })

    def post(self, request, id):
        order = Order.objects.get(id=id)
        form = LeaveFeedbackForm(request.POST)

        if form.is_valid():
            form.save(user=request.user, order=order)
            messages.success(request, "Thanks for your feedback, it was saved successfully !!!")
            return redirect(self.success_url)
        messages.error(request, "Some went wrong, please try, again...")
        return redirect("leave_feedback")


class ReadFeedbackView(View):
    template_name = "client_app/read_feedback.html"

    def get(self, request, id):
        order = Order.objects.get(id=id)
        feedback = Feedback.objects.get(order=order)
        return render(request, self.template_name, {
            "order": order,
            "feedback": feedback
        })
