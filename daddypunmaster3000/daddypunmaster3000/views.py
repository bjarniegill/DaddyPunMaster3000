from django.http import Http404
from django.views.generic import FormView, TemplateView

from daddypunmaster3000.forms import JokeForm
from daddypunmaster3000.models import Joke
from daddypunmaster3000.serializers import JokeSerializer


class Choose(TemplateView):
    template_name = 'templates/Choose.html'


class Jokes(TemplateView):
    template_name = 'templates/jokes.html'

    def dispatch(self, request, *args, **kwargs):
        group_id = int(args[0])
        if group_id < 1 or group_id > 2:
            raise Http404

        return super(Jokes, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        kwargs['group_id'] = self.args[0]
        return super(Jokes, self).get_context_data(**kwargs)


class AddJoke(FormView):
    template_name = 'templates/add_joke.html'
    form_class = JokeForm
    success_url = '/add/'

    def form_valid(self, form):
        joke = Joke(
            question=form.cleaned_data['question'],
            answer=form.cleaned_data['answer'],
            group_id=form.cleaned_data['group_id'],
        )
        joke.save()
        return super(AddJoke, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['group_1'] = Joke.objects.filter(group_id=1).count()
        kwargs['group_2'] = Joke.objects.filter(group_id=2).count()
        queryset = Joke.objects.all()
        serializer = JokeSerializer(queryset, many=True)
        kwargs['jokes'] = serializer.data

        return super(AddJoke, self).get_context_data(**kwargs)
