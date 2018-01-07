from django import forms
from django.core.exceptions import ValidationError

from daddypunmaster3000.models import GameSession


class JokeForm(forms.Form):

    question = forms.CharField(
        label='Question',
        max_length=None,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    answer = forms.CharField(
        label='Answer',
        max_length=None,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    group_id = forms.IntegerField(
        min_value=1,
        max_value=2,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class UseJokeForm(forms.Form):

    joke_id = forms.IntegerField(min_value=0)


class JoinSession(forms.Form):
    error_css_class = 'hello'

    session_id = forms.CharField(
        max_length=4,
        min_length=4,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def clean_session_id(self):
        session_id = self.cleaned_data['session_id']
        try:
            GameSession.objects.get(session_id=session_id)
        except GameSession.DoesNotExist:
            raise ValidationError('Session does not exist', code='invalid')

        return session_id
