from rest_framework import serializers


class JokeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question = serializers.CharField()
    answer = serializers.CharField()
    group_id = serializers.IntegerField()
