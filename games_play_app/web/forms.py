from django import forms

from games_play_app.web.models import Profile, Game


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')

        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileCreateForm(BaseProfileForm):
    pass


class ProfileDetailsForm(BaseProfileForm):
    pass


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hidden_fields()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __hidden_fields(self):
        for _,field in self.fields.items():
            field.widget=forms.HiddenInput()


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Title',
        #         }
        #     ),
        #     'rating': forms.FloatField(
        #
        #     )
        # }


class GameCreateForm(BaseGameForm):
    pass


class GameEditForm(BaseGameForm):
    pass


class GameDeleteForm(BaseGameForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()   # This deletes only the commit instance

        return self.instance

    # def save(self, commit=True):
    #     if commit:
    #         Game.objects.filter(game_id).delete()
    #         self.instance.delete()
    #
    #     return self.instance

    def _set_disabled_fields(self):
        for _,field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
