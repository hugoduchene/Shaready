from django.urls import  path
from api_user.views import (
    CreateSubscribe,
    GetAllInfoUser,
    ResearchUser,
    ResearchUser,
)

urlpatterns = [
    path('getresearchuser/<str:userSearch>', ResearchUser.as_view(), name="research_user"),
    path('postsubscription/<str:pseudoUser>', CreateSubscribe.as_view(), name="create_subscribed"),
    path('getallinfouser/<int:idUser>', GetAllInfoUser.as_view(), name="all_info_user"),
]
