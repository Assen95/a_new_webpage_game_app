from django import forms
from django.db.models import Avg
from django.shortcuts import render, redirect

from games_play_app.web.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from games_play_app.web.models import Profile, Game


def index(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'common/home-page.html', context)


def profile_create(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.all().get()
    game_count = Game.objects.count()
    average_rating = Game.objects.aggregate(Avg('rating'))

    context = {
        'profile': profile,
        'game_count': game_count,
        'average_rating': average_rating['rating__avg']
    }

    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.all().get()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.all().get()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/delete-profile.html', context)


def dashboard(request):
    profile = Profile.objects.first()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'common/dashboard.html', context)


def game_create(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'game/create-game.html', context)


def game_details(request, game_id):
    profile = Profile.objects.first()
    game = Game.objects.get(id=game_id)

    context = {
        'profile': profile,
        'game': game
    }
    return render(request, 'game/details-game.html', context)


def game_edit(request, game_id):
    profile = Profile.objects.first()
    game = Game.objects.filter(id=game_id).get()
    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form
    }
    return render(request, 'game/edit-game.html', context)


def game_delete(request, game_id):
    profile = Profile.objects.first()
    game = Game.objects.filter(id=game_id).get()
    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form
    }
    return render(request, 'game/delete-game.html', context)
