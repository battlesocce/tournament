from django.contrib import admin
from .models import player,totalteamrank,matchvideos,Property,PropertyImage,tournament,team,match,contestteam,contest_register_team,teamrank,highlights

admin.site.register(team)
admin.site.register(player)
admin.site.register(match)
admin.site.register(teamrank)
admin.site.register(highlights)
admin.site.register(contestteam)
admin.site.register(contest_register_team)
admin.site.register(tournament)
admin.site.register(matchvideos)
admin.site.register(totalteamrank)
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]

admin.site.register(Property, PropertyAdmin)
