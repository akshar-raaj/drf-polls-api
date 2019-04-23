from rest_framework import serializers

from .models import Question, Choice


class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    choice_text = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)


class ChoiceSerializerWithVotes(ChoiceSerializer):
    votes = serializers.IntegerField(read_only=True)


class QuestionListPageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()
    was_published_recently = serializers.BooleanField(read_only=True) # Serializer is smart enough to understand that was_published_recently is a method on Question
    choice = ChoiceSerializer(write_only=True)

    def create(self, validated_data):
        choice_dict = validated_data['choice']
        question = Question.objects.create(**validated_data)
        choice_dict['question'] = question
        Choice.objects.create(**choice_dict)
        return question


class QuestionDetailPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class QuestionResultPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializerWithVotes(many=True, read_only=True)
    max_voted_choice = ChoiceSerializerWithVotes(read_only=True)


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()
