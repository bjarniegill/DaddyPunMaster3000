from django import forms


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
