from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from .views import SignOutView, MyScheduleView, DateOrdersView


urlpatterns = [
    path("logout", SignOutView.as_view(), name="logout"),
    path("my_schedule", MyScheduleView.as_view(), name="my_schedule"),
    path("orders/<int:id>", DateOrdersView.as_view(), name="orders")
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
