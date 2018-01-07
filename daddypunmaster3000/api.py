import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from daddypunmaster3000.models import GameSession, Joke
from daddypunmaster3000.serializers import JokeSerializer
from daddypunmaster3000.utils import create_session


class RetrieveRandomJoke(APIView):

    def get_object(self, group_id, session_id):
        game_status = GameSession.objects.get(session_id=session_id)
        used_jokes_list = game_status.get_used_jokes()
        queryset = Joke.objects.filter(
            group_id=int(group_id)
        ).exclude(
            id__in=used_jokes_list
        )
        if not len(queryset):
            raise IndexError('No more unused jokes')

        return random.choice(queryset)

    def get(self, request, group_id, session_id):
        try:
            joke = self.get_object(group_id, session_id)
        except IndexError:
            return Response("", status.HTTP_204_NO_CONTENT)
        serializer = JokeSerializer(joke)

        return Response(serializer.data, status.HTTP_200_OK)


class CommitToJoke(APIView):

    def post(self, request):
        joke_id = int(request.data.get('joke_id'))
        session_id = request.data.get('session_id')
        game_session = GameSession.objects.get(session_id=session_id)
        try:
            game_session.set_joke_as_used(joke_id)
        except ValueError:
            return Response(
                "Joke has already been taken by another user.",
                status.HTTP_409_CONFLICT
            )

        return Response("", status.HTTP_200_OK)


class CreateSession(APIView):

    def get(self, request):
        random_id = create_session()

        return Response(random_id, status.HTTP_200_OK)