"""•	http://localhost:8000/ - home page
•	http://localhost:8000/profile/create - create profile page
•	http://localhost:8000/dashboard/ - dashboard page
•	http://localhost:8000/game/create/ - create game page
•	http://localhost:8000/game/details/<id>/ - details game page
•	http://localhost:8000/game/edit/<id>/ - edit game page
•	http://localhost:8000/game/delete/<id>/ - delete game page
•	http://localhost:8000/profile/details/ - details profile page
•	http://localhost:8000/profile/edit/ - edit profile page
•	http://localhost:8000/profile/delete/ - delete profile page
"""
from django.urls import path, include

from games_play_app.web.views import index, profile_create, profile_details, profile_edit, profile_delete, \
    dashboard, game_details, game_edit, game_delete, game_create

urlpatterns = (
    path('', index, name='index'),
    path('profile/', include([
        path('create/', profile_create, name='create profile'),
        path('details/', profile_details, name='details profile'),
        path('edit/', profile_edit, name='edit profile'),
        path('delete/', profile_delete, name='delete profile'),
    ])),
    path('dashboard/', dashboard, name='dashboard'),
    path('game/', include([
        path('create/', game_create, name='game create'),
        path('details/<int:game_id>/', game_details, name='game details'),
        path('edit/<int:game_id>/', game_edit, name='game edit'),
        path('delete/<int:game_id>/', game_delete, name='delete game')
    ])),
)