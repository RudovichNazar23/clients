from django.urls import path
from .views import SignOutView


urlpatterns = [
    path("logout", SignOutView.as_view(), name="logout"),


]

