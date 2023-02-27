from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from .views import SignOutView, MyScheduleView, WorkTimeOnDateView


urlpatterns = [
    path("logout", SignOutView.as_view(), name="logout"),
    path("my_schedule", MyScheduleView.as_view(), name="my_schedule"),
    path("my_schedule/time/<str:date>", WorkTimeOnDateView.as_view(), name="time")
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
