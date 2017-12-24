import json

from django.db import models


class Joke(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    group_id = models.PositiveIntegerField()


class GameStatus(models.Model):
    used_jokes = models.CharField(max_length=512, default='[]')

    def get_used_jokes(self):
        return json.loads(self.used_jokes)

    def set_joke_as_used(self, joke_id):
        used_jokes = json.loads(self.used_jokes)
        if joke_id in used_jokes:
            raise ValueError("This joke has been used by another user")
        used_jokes.append(int(joke_id))
        self.used_jokes = json.dumps(used_jokes)
        self.save()

