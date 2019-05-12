from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Question, Choice
from .serializers import QuestionListPageSerializer, QuestionDetailPageSerializer, QuestionChoiceSerializer, VoteSerializer, QuestionResultPageSerializer, ChoiceSerializer


class ChoicesView(ListCreateAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()


class QuestionsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    lookup_url_kwarg = 'question_id'

    def get_serializer_class(self):
        # Handle .create() requests
        if self.request.method == 'POST':
            return QuestionDetailPageSerializer
        # Handle .result() requests
        elif self.detail is True and self.request.method == 'GET' and self.name == 'Result':
            return QuestionResultPageSerializer
        # Handle .retrieve() requests
        elif self.detail is True and self.request.method == 'GET':
            return QuestionDetailPageSerializer
        return QuestionListPageSerializer

    @action(detail=True)
    def result(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    @action(methods=['GET', 'POST'], detail=True)
    def choices(self, request, *args, **kwargs):
        question = self.get_object()
        if request.method == 'GET':
            choices = question.choice_set.all()
            serializer = QuestionChoiceSerializer(choices, many=True)
            return Response(serializer.data)
        else:
            serializer = QuestionChoiceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(question=question)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['patch'], detail=True)
    def vote(self, request, *args, **kwargs):
        question = self.get_object()
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            choice = get_object_or_404(Choice, pk=serializer.validated_data['choice_id'], question=question)
            choice.votes += 1
            choice.save()
            return Response("Voted")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
