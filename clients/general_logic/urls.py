from django.urls import path
from .main import main


urlpatterns = [
    path("", main, name="main")



]



