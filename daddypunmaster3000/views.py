from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView

from daddypunmaster3000.forms import JoinSessionForm, JokeForm, ResetSessionForm
from daddypunmaster3000.models import Joke, GameSession
from daddypunmaster3000.serializers import JokeSerializer


class PickSession(FormView):
    template_name = 'templates/pick_session.html'
    form_class = JoinSessionForm
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            session_id = form.data.get('session_id')
            return redirect(GameSession.objects.get(session_id=session_id))

        return super(PickSession, self).form_valid(form)


class Choose(TemplateView):
    template_name = 'templates/choose.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            GameSession.objects.get(session_id=args[0])
        except GameSession.DoesNotExist:
            raise Http404

        return super(Choose, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Choose, self).get_context_data(**kwargs)
        context['session_id'] = self.args[0]

        return context


class Jokes(TemplateView):
    template_name = 'templates/jokes.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            GameSession.objects.get(session_id=args[0])
        except GameSession.DoesNotExist:
            raise Http404

        group_id = int(args[1])
        if group_id < 1 or group_id > 2:
            raise Http404

        return super(Jokes, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        kwargs['session_id'] = self.args[0]
        kwargs['group_id'] = self.args[1]

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


class ResetSessions(FormView):
    template_name = 'templates/reset_session.html'
    form_class = ResetSessionForm
    success_url = '/reset/'

    def form_valid(self, form):
        if form.is_valid():
            reset_key = form.data.get('reset_key')
            if reset_key == "penis":
                GameSession.objects.all().delete()

        return super(ResetSessions, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ResetSessions, self).get_context_data(**kwargs)
        context['sessions'] = GameSession.objects.all()

        return context