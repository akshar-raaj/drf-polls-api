from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status

from .models import Question, Choice
from .serializers import QuestionListPageSerializer, QuestionDetailPageSerializer, QuestionChoiceSerializer, VoteSerializer, QuestionResultPageSerializer, ChoiceSerializer


class QuestionsView(ListCreateAPIView):

    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionListPageSerializer
        else:
            return QuestionDetailPageSerializer


class QuestionDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionDetailPageSerializer
    lookup_url_kwarg = 'question_id'
    queryset = Question.objects.all()


class QuestionChoicesView(APIView):
    
    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['question_id'])
        choices = question.choice_set.all()
        serializer = QuestionChoiceSerializer(choices, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['question_id'])
        serializer = QuestionChoiceSerializer(data=request.data)
        if serializer.is_valid():
            choice = serializer.save(question=question)
            return Response("Choice created with id %s" % (choice.id), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChoicesView(APIView):

    def get(self, request, *args, **kwargs):
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            choice = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoteView(APIView):

    def patch(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['question_id'])
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            choice = get_object_or_404(Choice, pk=serializer.validated_data['choice_id'], question=question)
            choice.votes += 1
            choice.save()
            return Response("Voted")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionResultView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionResultPageSerializer
    lookup_url_kwarg = 'question_id'
