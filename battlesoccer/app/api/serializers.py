from rest_framework import serializers
from app.models import team,totalteamrank,PropertyImage,matchvideos,player,tournament,Property,teamrank,highlights,match,contestteam,contest_register_team,Answer
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class TeamAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = team
        fields = ("logo", "coverpic",)



class PlayerAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = player
        fields = ("pic",)



class TeamdataSerializer(serializers.ModelSerializer):
    coverpic = serializers.ImageField(read_only=True)
    logo = serializers.ImageField(read_only=True)

    

    class Meta:
        model = team
        fields = "__all__" 


class PlayerSerializer(serializers.ModelSerializer):

    teamname = serializers.StringRelatedField(read_only=True)
    pic = serializers.ImageField(read_only=True)
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    own = TeamdataSerializer(source='teamname',read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = player
        exclude = ["voters"]

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_likes_count(self, instance):
        return instance.voters.count()



class HighlightsSerializer(serializers.ModelSerializer):
    teamname = serializers.StringRelatedField(read_only=True)
    own = TeamdataSerializer(source='teamname',read_only=True)
    answers_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    tournament_name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = highlights
        exclude = ["highlightsvoters"]


    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.highlightsvoters.filter(pk=request.user.pk).exists()

    def get_answers_count(self, instance):
        return instance.answers.count()
    
    def get_likes_count(self, instance):
        return instance.highlightsvoters.count()


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    highlight_id = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ["highlight", "Answervoters", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, instance):
        return instance.Answervoters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.Answervoters.filter(pk=request.user.pk).exists()

    def get_highlight_id(self, instance):
        return instance.highlight.id




class ContestSerializer(serializers.ModelSerializer):
    own = TeamdataSerializer(source='teamown',read_only=True)

    class Meta:
        model = contestteam
        fields = "__all__"


class Contest_register_team_Serializer(serializers.ModelSerializer):

    class Meta:
        model = contest_register_team
        fields = "__all__"


class MacthplayedSerializer(serializers.ModelSerializer):
    team_a = serializers.StringRelatedField(read_only=True)
    team_b = serializers.StringRelatedField(read_only=True)
    tournament_name = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = match
        fields = "__all__"
     

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    videos = HighlightsSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    coverpic = serializers.ImageField(read_only=True)
    logo = serializers.ImageField(read_only=True)
    belongs = MacthplayedSerializer(many=True, read_only=True)
    active = serializers.SerializerMethodField(read_only=True)

    # Use this method for the custom field
    def get_active(self, instance):
        request = self.context.get('request')
        return instance.user.is_activated

    class Meta:
        model = team
        fields = "__all__"


class TeamdataSerializer(serializers.ModelSerializer):
    coverpic = serializers.ImageField(read_only=True)
    logo = serializers.ImageField(read_only=True)

    class Meta:
        model = team
        fields = "__all__" 



class TeamRankSerializer(serializers.ModelSerializer):
    own = TeamdataSerializer(source='teamown',read_only=True)
    tournament_name = serializers.StringRelatedField(read_only=True)
    teamown = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = teamrank
        fields = ['tournament_name','teamown','teamname','teamgoals',
        'match_lost','matchs_played','match_won','own']



class totalTeamRankSerializer(serializers.ModelSerializer):
    own = TeamdataSerializer(source='teamown',read_only=True)
    tournament_name = serializers.StringRelatedField(read_only=True)
    teamown = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = totalteamrank
        fields = ['tournament_name','teamown','teamname','teamgoals',
        'match_lost','matchs_played','match_won','own']



class gallerypicsSerializer(serializers.ModelSerializer):
    tournament_id= serializers.CharField(source="property.tournament_name.id")
    property=serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PropertyImage
        fields = "__all__"


class gallerySerializer(serializers.ModelSerializer):
    tournament_name = serializers.StringRelatedField(read_only=True)
    images=gallerypicsSerializer(many=True, read_only=True)
    class Meta:
        model = Property
        fields = "__all__"


class tournamentSerializer(serializers.ModelSerializer):
    rank = TeamRankSerializer(many=True, read_only=True)
    tour_player_detail= serializers.CharField(source="tour_player.player")
    tour_goalkeaper_detail = serializers.CharField(source="tour_goalkeaper.player")
    tour_highgoals_detail = serializers.CharField(source="tour_highgoals.player")
    tour_fairplay_detail = serializers.CharField(source="tour_fairplay.player")
    tour_moves_detail = serializers.CharField(source="tour_moves.player")

    class Meta:
        model = tournament
        fields = "__all__" 

class matchvideosSerializer(serializers.ModelSerializer):
    tournament_name = serializers.StringRelatedField(read_only=True)
    team_a= serializers.StringRelatedField(read_only=True)
    team_b = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = matchvideos
        fields = "__all__" 



