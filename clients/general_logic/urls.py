from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .main import Main


urlpatterns = [
    path("", Main.as_view(), name="main")

]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
