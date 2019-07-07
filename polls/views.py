from rest_framework import generics
from rest_framework import filters

from .models import Question
from .serializers import QuestionSerializer


class SearchFilterWithSpaces(filters.SearchFilter):
    def get_search_terms(self, request):
        params = request.query_params.get(self.search_param, '')
        terms =  params.split(",")
        return [term.strip() for term in terms]


class QuestionsAPIView(generics.ListCreateAPIView):
    search_fields = ['^question_text', 'author']
    filter_backends = (filters.SearchFilter,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
