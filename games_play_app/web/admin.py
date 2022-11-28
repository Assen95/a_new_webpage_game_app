from django.contrib import admin

from games_play_app.web.models import Profile, Game


# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Game)
class AdminGame(admin.ModelAdmin):
    pass