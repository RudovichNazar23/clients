from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import RegistrationView

urlpatterns = [
    path("registration", RegistrationView.as_view(), name="registration"),



]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )