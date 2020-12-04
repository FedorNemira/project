from django.urls import path
from poll.views import PollView

app_name = "poll"

urlpatterns = [
    path('polls/', PollView.as_view()),
]