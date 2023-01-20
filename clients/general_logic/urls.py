from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .main import main


urlpatterns = [
    path("", main, name="main")

]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
