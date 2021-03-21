from django import forms
from .models import Animes

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Animes
        fields = '__all__'

    def clean_lancamento(self):
        lancamento = self.cleaned_data['lancamento']
        if int(lancamento) < 1972 or int(lancamento) > 2020:
            raise forms.ValidationError('Nenhum Anime foi lançado nesse ano!')
        return lancamento