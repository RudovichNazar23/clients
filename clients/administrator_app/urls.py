from django.urls import path
from .views import SignOutView, CreateServiceView, WorkerListView, WorkerProfileView


urlpatterns = [
    path("logout", SignOutView.as_view(), name="logout"),
    path("create_service", CreateServiceView.as_view(), name="create_service"),
    path("worker_list", WorkerListView.as_view(), name="worker_list"),
    path("worker_list/worker/<str:first_name>", WorkerProfileView.as_view(), name="worker")


]

