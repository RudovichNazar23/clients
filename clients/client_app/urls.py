from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import RegistrationView, MyProfileView

urlpatterns = [
    path("registration", RegistrationView.as_view(), name="registration"),
    path("my_profile", MyProfileView.as_view(), name="my_profile"),



]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )