from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet, ModelViewSet

from .models import Question, Choice
from .serializers import QuestionListPageSerializer, QuestionDetailPageSerializer, QuestionChoiceSerializer, VoteSerializer, QuestionResultPageSerializer, ChoiceSerializer


class AnotherQuestionsView(ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailPageSerializer
    lookup_url_kwarg = 'question_id'


class QuestionsView(ListCreateAPIView):

    queryset = Question.objects.all()
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionListPageSerializer
        else:
            return QuestionDetailPageSerializer


class QuestionDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionDetailPageSerializer
    lookup_url_kwarg = 'question_id'
    queryset = Question.objects.all()


class QuestionChoicesView(ListCreateAPIView):
    serializer_class = QuestionChoiceSerializer

    def get_queryset(self):
        question = get_object_or_404(Question, pk=self.kwargs['question_id'])
        return question.choice_set.all()

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs['question_id'])
        serializer.save(question=question)


class ChoicesView(ListCreateAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()


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


class YetAnotherQuestionsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailPageSerializer
    lookup_url_kwarg = 'question_id'
