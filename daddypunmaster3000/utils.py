import datetime
import random
import string

from daddypunmaster3000.models import GameSession


def create_session():

    while True:
        random_id = ''.join(
            random.choice(string.ascii_lowercase + string.digits)
            for _ in range(4)
        )
        try:
            GameSession.objects.get(session_id=random_id)
        except GameSession.DoesNotExist:
            game_status = GameSession(session_id=random_id)
            game_status.save()

            return random_id


def delete_old_sessions():

    sessions = GameSession.objects.all()
    for session in sessions:
        session_delta_date = session.updated + datetime.timedelta(days=1)
        session_naive = session_delta_date.replace(tzinfo=None)
        if session_naive < datetime.datetime.now().replace(tzinfo=None):
            session.delete()
