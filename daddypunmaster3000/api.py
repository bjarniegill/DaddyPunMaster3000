import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from daddypunmaster3000.models import GameStatus, Joke
from daddypunmaster3000.serializers import JokeSerializer
from daddypunmaster3000.utils import get_game_status


class RetrieveRandomJoke(APIView):

    def get_object(self, group_id):
        game_status = get_game_status()
        used_jokes_list = game_status.get_used_jokes()
        queryset = Joke.objects.filter(
            group_id=int(group_id)
        ).exclude(
            id__in=used_jokes_list
        )
        if not len(queryset):
            raise IndexError('No more unused jokes')

        return random.choice(queryset)

    def get(self, request, group_id, format=None):
        try:
            joke = self.get_object(group_id)
        except IndexError:
            return Response("", status.HTTP_204_NO_CONTENT)
        serializer = JokeSerializer(joke)

        return Response(serializer.data)


class CommitToJoke(APIView):

    def post(self, request):
        joke_id = int(request.data.get('joke_id'))
        game_status = get_game_status()
        try:
            game_status.set_joke_as_used(joke_id)
        except ValueError:
            return Response(
                "Joke has already been taken by another user.",
                status.HTTP_409_CONFLICT
            )

        return Response("", status.HTTP_200_OK)
