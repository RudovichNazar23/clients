from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from .views import SignOutView


urlpatterns = [
    path("logout", SignOutView.as_view(), name="logout"),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
