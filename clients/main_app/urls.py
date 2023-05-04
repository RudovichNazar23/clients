from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .main import Main, ClientProfileView


urlpatterns = [
    path("", Main.as_view(), name="main"),
    path("client_profile/<str:first_name>", ClientProfileView.as_view(), name="client_profile")

]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
