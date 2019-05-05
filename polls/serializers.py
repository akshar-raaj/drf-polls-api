from rest_framework import serializers

from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id', 'choice_text')


class ChoiceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('choice_text', 'question')


class ChoiceSerializerWithVotes(ChoiceSerializer):

    class Meta(ChoiceSerializer.Meta):
        fields = ChoiceSerializer.Meta.fields + ('votes',)


class QuestionListPageSerializer(serializers.ModelSerializer):

    was_published_recently = serializers.BooleanField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionDetailPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializer(read_only=True, many=True)


class QuestionResultPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializerWithVotes(many=True, read_only=True)


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()
