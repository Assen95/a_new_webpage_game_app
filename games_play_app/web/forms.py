from django import forms

from games_play_app.web.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email','age', 'password')