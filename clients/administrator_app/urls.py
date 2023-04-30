from django.urls import path
from .views import SignOutView, CreateServiceView, WorkerListView, WorkerProfileView, CreateWorkDayView, CreateWorkdayAssignment, DeactivateOrderView, WorkerScheduleView


urlpatterns = [
    path("logout", SignOutView.as_view(), name="logout"),
    path("create_service", CreateServiceView.as_view(), name="create_service"),
    path("worker_list", WorkerListView.as_view(), name="worker_list"),
    path("worker_list/worker/<str:first_name>", WorkerProfileView.as_view(), name="worker"),
    path("create_workday", CreateWorkDayView.as_view(), name="create_workday"),
    path("create_assignment", CreateWorkdayAssignment.as_view(), name="create_assignment"),
    path("deactivate_order/<int:id>", DeactivateOrderView.as_view(), name="deactivate_order"),
    path("worker_schedule/<str:first_name>", WorkerScheduleView.as_view(), name="worker_schedule"),
]

