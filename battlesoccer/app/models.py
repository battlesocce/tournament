from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission, User
from django.utils.text import slugify
from django_resized import ResizedImageField
from django.contrib.auth.models import UserManager
from django.db.models import Sum
from django.core.validators import MaxValueValidator
from django.conf import settings
import random


class team(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    passcode = models.CharField(max_length=10, blank=True, null=True)
    teamname = models.CharField(max_length=100, blank=True, null=True,default="Team name")
    logo = ResizedImageField(size=[300, 300], crop=['middle', 'center'], quality=100, blank=True,default="soccer_logo.jpeg")
    coverpic = ResizedImageField(size=[800, 350], crop=['middle', 'center'], quality=100, null=True,blank=True,default='soccer.jpeg')
    teamquotes = models.CharField(max_length=20000, default='hey!I am ready for the battle', null=True, blank=True)
    teamcontact = models.IntegerField(blank=True,null=True)
    teamcity = models.CharField(max_length=200, default='unknown', null=True, blank=True)


    def __str__(self):
        return str(self.teamname)


class player(models.Model):
    teamname = models.ForeignKey(team, on_delete=models.CASCADE, related_name="players")
    player = models.CharField(max_length=100, blank=True, null=True)
    playerpasscode = models.IntegerField(default='0000', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    contact = models.IntegerField(blank=True,null=True)
    goals = models.IntegerField(blank=True, null=True,default='0',)
    profession = models.CharField(max_length=100, blank=True, null=True)
    facebookurl = models.CharField(max_length=100,blank=True, null=True)
    instaurl = models.CharField(max_length=100,blank=True, null=True)
    position = models.CharField(default='unknown', max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, default='hey! i am a battle soccer player', blank=True, null=True)
    pic = ResizedImageField(size=[300, 300], crop=['middle', 'center'], quality=100,default="woman-playing.png")
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votes")
    def __str__(self):
        return str(self.player)



class tournament(models.Model):
    tour_date= models.DateField(auto_now_add=True,blank=True, null=True)
    tour_name = models.CharField(max_length=200,default=1)
    tour_coverpic=ResizedImageField(size=[800, 200], crop=['middle', 'center'], quality=100, null=True,blank=True)
    tour_city = models.CharField(max_length=200,default=1)
    tour_price = models.IntegerField(max_length=200,default=1)


    
    tour_player=models.ForeignKey(player,default=1, on_delete=models.CASCADE,related_name="bestplayer")
    tour_goalkeaper=models.ForeignKey(player,default=1, on_delete=models.CASCADE,related_name="goalkeaper")
    tour_highgoals=models.ForeignKey(player,default=1, on_delete=models.CASCADE,related_name="highgoals")
    tour_fairplay=models.ForeignKey(player,default=1, on_delete=models.CASCADE,related_name="defender")
    tour_moves=models.ForeignKey(player,default=1, on_delete=models.CASCADE,related_name="moves")  

    def __str__(self):
        return str(self.tour_name)


class match(models.Model):
    tournament_name= models.ForeignKey(tournament,default=1, on_delete=models.CASCADE,related_name='tour')
    team_a= models.ForeignKey(team,default=1, on_delete=models.CASCADE,related_name='belongs')
    team_b= models.ForeignKey(team,default=1, on_delete=models.CASCADE)
    team_a_goals=models.IntegerField()
    team_b_goals=models.IntegerField()
    date=models.DateField(blank=True, null=True)
    time=models.TimeField(blank=True, null=True)
    winner=models.CharField(max_length=200)


    def __str__(self):
        return str(self.team_a)


class teamrank(models.Model):
    tournament_name= models.ForeignKey(tournament,default=1, on_delete=models.CASCADE,related_name='rank')
    teamown = models.ForeignKey(team,default=1, on_delete=models.CASCADE)
    teamname=models.CharField(max_length=200,default=1)
    teamgoals=models.IntegerField()
    matchs_played=models.IntegerField()
    match_won=models.IntegerField()
    match_lost=models.IntegerField()

    def __str__(self):
        return str(self.teamname)

class totalteamrank(models.Model):
    teamown = models.ForeignKey(team,default=1, on_delete=models.CASCADE)
    teamname=models.CharField(max_length=200,default=1)
    teamgoals=models.IntegerField()
    matchs_played=models.IntegerField()
    match_won=models.IntegerField()
    match_lost=models.IntegerField()

    def __str__(self):
        return str(self.teamname)



class highlights(models.Model):
    tournament_name= models.ForeignKey(tournament,default=1, on_delete=models.CASCADE,related_name='tourhighlight')
    teamname= models.ForeignKey(team,default=None, on_delete=models.CASCADE,related_name="videos")
    highlight=models.URLField();
    highlightsvoters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="highlightsvotes")

    def __str__(self):
        return str(self.teamname)


class matchvideos(models.Model):
    tournament_name= models.ForeignKey(tournament,default=1, on_delete=models.CASCADE,related_name='tourmatchvideos')
    team_a= models.ForeignKey(team,default=1, on_delete=models.CASCADE,related_name='team_a')
    team_b= models.ForeignKey(team,default=1, on_delete=models.CASCADE,related_name='team_b')
    matchvideos=models.URLField();
    

    def __str__(self):
        return str(self.tournament_name)


class Property(models.Model):
    tournament_name= models.ForeignKey(tournament,default=1, on_delete=models.CASCADE,related_name='tourpics')
    
    def __str__(self):
        return str(self.tournament_name)

class PropertyImage(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE, related_name='images')
    image = ResizedImageField(size=[500, 500], crop=['middle', 'center'],quality=100)
 

class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    highlight = models.ForeignKey(highlights,
                                 on_delete=models.CASCADE,
                                 related_name="answers")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    Answervoters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="Answervotes")

    def __str__(self):
        return str(self.author.username)



class contestteam(models.Model):
    teamown = models.OneToOneField(team,default=1, on_delete=models.CASCADE)
    teamcontact = models.IntegerField(blank=True,null=True)
    contactname=models.CharField(max_length=200,default=1)


    def __str__(self):
        return str(self.teamown)

class contest_register_team(models.Model):
    contest_teamname = models.CharField(max_length=200,default=1)
    contest_teamcontact = models.IntegerField(blank=True,null=True)
    contest_adminname=models.CharField(max_length=200,default=1)
    contest_team_id=models.IntegerField(blank=True,null=True,default=0)

    def __str__(self):
        return str(self.contest_teamname)