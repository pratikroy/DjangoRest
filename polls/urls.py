from django.urls import path, include
from polls import apiviews

urlpatterns = [
    path("polls/", apiviews.PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", apiviews.PollDetail.as_view(), name="poll_detail"),
]
