from django.urls import include, path
from rest_framework.routers import DefaultRouter
from app.api.views import (TeamViewSet,TeamRankViewSetall,MatchplayedViewSet,
PlayerLikeAPIView,ContestViewSetcheck,singletournamentViewSetall,alltournamentViewSetall,totalTeamRankViewSet,matchvideosViewSet,gallerypicsViewSet,tournamentViewSetall,galleryViewSet,SingleHighlightViewSet,HighlightsLikeAPIView,AnswerRUDAPIView,AnswerCreateAPIView,AnswerListAPIView,HighlightsViewSet,AnswerLikeAPIView,ContestViewSet,AvatarUpdateView,TeamRankViewSet,PlayerViewSet,PlayerpicUpdateView,Contest_register_team_viewset)

router = DefaultRouter()
router.register(r"team", TeamViewSet, basename="team")
router.register(r"player", PlayerViewSet, basename="player")
router.register(r"contest", ContestViewSet, basename="contest")
router.register(r"contestcheck", ContestViewSetcheck, basename="contestcheck")
router.register(r"contest_register", Contest_register_team_viewset, basename="contest_register")



urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update"),
    path("highlights/", HighlightsViewSet.as_view(), name="highlights"),
    path("matchvideos/", matchvideosViewSet.as_view(), name="matchvideosViewSet"),
    path("highlights/<int:pk>/", SingleHighlightViewSet.as_view(), name="singlehighlights"),
    path("teamrank/", TeamRankViewSet.as_view(), name="teamrank"),
    path("gallery/", galleryViewSet.as_view(), name="gallery"),
    path("gallerypics/", gallerypicsViewSet.as_view(), name="gallerypics"),
    path("teamrankall/", TeamRankViewSetall.as_view(), name="teamrankall"),
    path("totalteamrankall/",totalTeamRankViewSet.as_view(), name="totalteamrankall"),
    path("tournament/", tournamentViewSetall.as_view(), name="tour"),
    path("tournament/<int:pk>/", singletournamentViewSetall.as_view(), name="idtour"),
    path("alltournament/", alltournamentViewSetall.as_view(), name="alltour"),
    path("matchplayed/", MatchplayedViewSet.as_view(), name="matchplayed"),
    path("playerpic/<int:pk>/", PlayerpicUpdateView.as_view(), name="playerpic-update"),
    path("playerlike/<int:pk>/like/",PlayerLikeAPIView.as_view(), name="player-like"),
    path("answers/<int:pk>/",AnswerRUDAPIView.as_view(),name="answer-detail"),
    path("answers/<int:pk>/like/",AnswerLikeAPIView.as_view(), name="answer-like"),
    path("highlights/<int:pk>/answer/", AnswerCreateAPIView.as_view(),name="answer-create"),
    path("highlights/<int:pk>/answers/", AnswerListAPIView.as_view(),name="answer-list"),
    path("highlights/<int:pk>/like/",HighlightsLikeAPIView.as_view(), name="answer-like"),

]