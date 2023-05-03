from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import RegistrationView, MyProfileView, LoginView, SignOutView, WorkerProfileView, ServiceProfileView, OrderServiceView, MyVisitsView, LeaveFeedBackView, ReadFeedbackView, WorkerFeedbacksView


urlpatterns = [
    path("registration", RegistrationView.as_view(), name="registration"),
    path("my_profile", MyProfileView.as_view(), name="my_profile"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", SignOutView.as_view(), name="logout"),
    path("worker_info/<str:first_name>", WorkerProfileView.as_view(), name="worker_info"),
    path("worker_feedbacks/<str:first_name>", WorkerFeedbacksView.as_view(), name="worker_feedbacks"),
    path("service_info/<str:name>", ServiceProfileView.as_view(), name="service_info"),
    path("order_service", OrderServiceView.as_view(), name="order_service"),
    path("my_visits", MyVisitsView.as_view(), name="my_visits"),
    path("leave_feedback/<int:id>", LeaveFeedBackView.as_view(), name="leave_feedback"),
    path("read_feedback/<int:id>", ReadFeedbackView.as_view(), name="read_feedback")
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
