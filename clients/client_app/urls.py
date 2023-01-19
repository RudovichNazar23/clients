from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import RegistrationView, MyProfileView, LoginView, SignOutView, MainPageView


urlpatterns = [
    path("registration", RegistrationView.as_view(), name="registration"),
    path("my_profile", MyProfileView.as_view(), name="my_profile"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", SignOutView.as_view(), name="logout"),
    path("main", MainPageView.as_view(), name="main")


]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )