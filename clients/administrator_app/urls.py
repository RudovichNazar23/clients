from django.urls import path
<<<<<<< HEAD
from .views import SignOutView, CreateServiceView

urlpatterns = [
    path("logout", SignOutView.as_view(), name="logout"),
    path("create_service", CreateServiceView.as_view(), name="create_service")
=======
from .views import SignOutView


urlpatterns = [
    path("logout", SignOutView.as_view(), name="logout"),

>>>>>>> 3ca1b3cbed2543f70acb0b58b31105c089c3c1fd

]

