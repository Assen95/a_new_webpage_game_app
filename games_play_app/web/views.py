from django.shortcuts import render


def index(request):
    return render(request, 'common/home-page.html')


def profile_create(request):
    return render(request, 'profile/create-profile.html')


def profile_details(request):
    return render(request, 'profile/details-profile.html')


def profile_edit(request):
    return render(request, 'profile/edit-profile.html')


def profile_delete(request):
    return render(request, 'profile/delete-profile.html')


def dashboard(request):
    return render(request, 'common/dashboard.html')


def game_create(request):
    return render(request, 'game/create-game.html')


def game_details(request, game_id):
    return render(request, 'game/details-game.html')


def game_edit(request, game_id):
    return render(request, 'game/edit-game.html')


def game_delete(request, game_id):
    return render(request, 'game/delete-game.html')
