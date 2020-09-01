from django.urls import path
from api_user.views import (
    CreateSubscribe,
    GetAllInfoUser,
    ResearchUser,
    AlreadySubscribed,
    NbsUser,
)

urlpatterns = [
    path('getresearchuser/<str:userSearch>', ResearchUser.as_view(), name="research_user"),
    path('postsubscription/<str:pseudoUser>', CreateSubscribe.as_view(), name="create_subscribed"),
    path('getallinfouser/<int:idUser>', GetAllInfoUser.as_view(), name="all_info_user"),
    path('alreadysubscribe/<int:idReceiving>', AlreadySubscribed.as_view(), name="already_sub"),
    path('nbsuser', NbsUser.as_view(), name="nbs_user"),
]
