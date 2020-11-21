from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import generics, status, viewsets
from django.db.models import Prefetch


from app.api.pagination import SmallSetPagination,fourSetPagination,fiveSetPagination

from app.api.permissions import IsOwnerOrReadOnly, IsOwnProfileOrReadOnly
from app.api.serializers import (TeamSerializer,matchvideosSerializer,gallerySerializer,tournamentSerializer,ContestSerializer,HighlightsSerializer,TeamRankSerializer,TeamAvatarSerializer,
                                      PlayerSerializer,totalTeamRankSerializer,gallerypicsSerializer,PlayerAvatarSerializer,MacthplayedSerializer,Contest_register_team_Serializer,AnswerSerializer
                                      )
from app.models import team,Property,matchvideos,totalteamrank,PropertyImage,contestteam,tournament,player,teamrank,highlights,match,contest_register_team,Answer



class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = TeamAvatarSerializer

    def get_object(self):
        team_object = self.request.user.team
        return team_object


class PlayerpicUpdateView(generics.UpdateAPIView):
    serializer_class = PlayerAvatarSerializer

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        player_object = get_object_or_404(player,pk=pk)
        return player_object



class TeamViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = TeamSerializer
    queryset = team.objects.all().order_by('-id')
    permission_classes = [IsOwnProfileOrReadOnly]
    pagination_class = fourSetPagination


    def get_queryset(self):
        queryset = team.objects.all().order_by('-id')
        queryset = queryset.filter(user__is_active=1)
        return queryset

class ContestViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = contestteam.objects.all()
    serializer_class = ContestSerializer
    pagination_class = fourSetPagination


class ContestViewSetcheck(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = contestteam.objects.all()
    serializer_class = ContestSerializer



class TeamRankViewSet(generics.ListAPIView):
    queryset = teamrank.objects.all().order_by('-match_won','-teamgoals')
    lookup_field = "team_a"
    serializer_class = TeamRankSerializer
    pagination_class = fourSetPagination

class totalTeamRankViewSet(generics.ListAPIView):
    queryset = totalteamrank.objects.all().order_by('-match_won','-teamgoals')
    lookup_field = "team_a"
    serializer_class = totalTeamRankSerializer

class matchvideosViewSet(generics.ListAPIView):
    queryset = matchvideos.objects.all()
    lookup_field = "tournament_name"
    serializer_class = matchvideosSerializer
    pagination_class = fiveSetPagination

class galleryViewSet(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = gallerySerializer


class gallerypicsViewSet(generics.ListAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = gallerypicsSerializer

class TeamRankViewSetall(generics.ListAPIView):
    queryset = teamrank.objects.all().order_by('-match_won','-teamgoals','matchs_played')
    lookup_field = "team_a"
    serializer_class = TeamRankSerializer


class tournamentViewSetall(generics.ListAPIView):
    queryset = tournament.objects.all()
    queryset = tournament.objects.prefetch_related(Prefetch(
        'rank',
        queryset=teamrank.objects.order_by('-match_won','-teamgoals','matchs_played')))
    lookup_field = "tour_name"
    serializer_class = tournamentSerializer
    pagination_class = fourSetPagination


class alltournamentViewSetall(generics.ListAPIView):
    queryset = tournament.objects.all()
    queryset = tournament.objects.prefetch_related(Prefetch(
        'rank',
        queryset=teamrank.objects.order_by('-match_won','-teamgoals','matchs_played')))
    lookup_field = "tour_name"
    serializer_class = tournamentSerializer



class MatchplayedViewSet(generics.ListAPIView):
    queryset = match.objects.all()
    lookup_field = "team_a"
    serializer_class = MacthplayedSerializer


class HighlightsViewSet(generics.ListAPIView):
    queryset = highlights.objects.all()
    lookup_field = "id"
    serializer_class = HighlightsSerializer
    pagination_class = fiveSetPagination

class HighlightsLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an answer instance."""
    serializer_class = HighlightsSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an answer instance."""
        highlight = get_object_or_404(highlights, pk=pk)
        user = request.user

        highlight.highlightsvoters.remove(user)
        highlight.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(highlight, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an answer instance."""
        highlight = get_object_or_404(highlights, pk=pk)
        user = request.user

        highlight.highlightsvoters.add(user)
        highlight.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(highlight, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)



class SingleHighlightViewSet(generics.ListAPIView):
    """Provide the answers queryset of a specific question instance."""
    serializer_class = HighlightsSerializer

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("pk")
        return highlights.objects.filter(id=kwarg_slug)

class singletournamentViewSetall(generics.ListAPIView):
   
    lookup_field = "id"
    serializer_class = tournamentSerializer

    
    def get_queryset(self):
        kwarg_slug = self.kwargs.get("pk")
        queryset = tournament.objects.filter(id=kwarg_slug).prefetch_related(Prefetch(
        'rank',
        queryset=teamrank.objects.order_by('-match_won','-teamgoals','matchs_played')))
        return queryset

    




class Contest_register_team_viewset(ModelViewSet):
    queryset = contest_register_team.objects.all()
    serializer_class = Contest_register_team_Serializer
    lookup_field = "contest_teamname"


class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    lookup_field = "id"
    filter_backends = [SearchFilter]
    search_fields = ["player"]
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = fourSetPagination
    queryset = player.objects.all()



    def perform_create(self, serializer):
        teamname = self.request.user.team
        serializer.save(teamname=teamname)

class AnswerCreateAPIView(generics.CreateAPIView):
    """Allow users to answer a question instance if they haven't already."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("pk")
        highlight = get_object_or_404(highlights, id=kwarg_slug)

        serializer.save(author=request_user, highlight=highlight)

class AnswerListAPIView(generics.ListAPIView):
    """Provide the answers queryset of a specific question instance."""
    serializer_class = AnswerSerializer
    pagination_class = SmallSetPagination

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("pk")
        return Answer.objects.filter(highlight_id=kwarg_slug).order_by("-created_at")


class AnswerLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an answer instance."""
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an answer instance."""
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user

        answer.Answervoters.remove(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an answer instance."""
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user

        answer.Answervoters.add(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)



class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an answer instance to it's author."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]



class PlayerLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an answer instance."""
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]


    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an answer instance."""
        players = get_object_or_404(player, pk=pk)
        user = request.user

        players.voters.remove(user)
        players.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(players, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an answer instance."""
        players = get_object_or_404(player, pk=pk)
        user = request.user

        players.voters.add(user)
        players.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(players, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

