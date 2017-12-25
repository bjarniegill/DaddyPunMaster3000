from daddypunmaster3000.models import GameStatus


def get_game_status():
    objects = GameStatus.objects.all()
    if len(objects) > 1:
        raise ValueError('There is more than one GameStatus object')
    elif len(objects) == 1:
        game_status = objects.first()
    else:
        game_status = GameStatus()
        game_status.save()

    return game_status

