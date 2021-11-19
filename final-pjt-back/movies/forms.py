from django import forms
from .models import Rank, SelectGenre


class RankForm(forms.ModelForm):
    
    class Meta:
        model = Rank
        fields = ['rank', 'content']

class SelectGenreForm(forms.ModelForm):

    class Meta:
        model = SelectGenre
        fields = ['selected_genre']