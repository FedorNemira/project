from django.urls import path
from poll.views import PollView
from poll.views import QuestionView

app_name = "poll"

urlpatterns = [
    path('polls/', PollView.as_view()),
    path('questions/', QuestionView.as_view()),

]