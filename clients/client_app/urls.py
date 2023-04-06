from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import RegistrationView, MyProfileView, LoginView, SignOutView, MainPageView, WorkerProfileView, ServiceProfileView


urlpatterns = [
    path("registration", RegistrationView.as_view(), name="registration"),
    path("my_profile", MyProfileView.as_view(), name="my_profile"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", SignOutView.as_view(), name="logout"),
    path("main", MainPageView.as_view(), name="main"),
    path("worker_info/<str:first_name>", WorkerProfileView.as_view(), name="worker_info"),
    path("service_info/<str:name>", ServiceProfileView.as_view(), name="service_info")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
