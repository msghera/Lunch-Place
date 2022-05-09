from poll.models import Poll, Vote
from rest_framework .serializers import ModelSerializer
from rest_framework.validators import ValidationError

import datetime


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

    def validate(self, attr):
        is_exist = Poll.objects.filter(
            poll_date=datetime.date.today()
        ).exists()
        if is_exist:
            raise ValidationError('Poll already exists for today.')

        return attr


class ResultSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ('winner_menu_id',)


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
