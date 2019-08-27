from django.urls import path, include
from polls import apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("pollset", apiviews.PollViewSet, base_name="pollset")


urlpatterns = [
    path("polls/", apiviews.PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", apiviews.PollDetail.as_view(), name="poll_detail"),
    path("polls/<int:pk>/choices/",
        apiviews.ChoiceList.as_view(),
        name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",
        apiviews.CreateVote.as_view(),
        name="create_vote"),
    path("users/", apiviews.UserCreate.as_view(), name="user_create"),
    path("login/", apiviews.LoginView.as_view(), name="login"),
]

urlpatterns += router.urls
