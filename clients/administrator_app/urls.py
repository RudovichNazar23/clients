from django.urls import path
from .views import SignOutView, CreateServiceView

urlpatterns = [
    path("logout", SignOutView.as_view(), name="logout"),
    path("create_service", CreateServiceView.as_view(), name="create_service")

]

