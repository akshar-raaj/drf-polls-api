from rest_framework import generics
from rest_framework import filters

from .models import Question
from .serializers import QuestionSerializer


class SearchFilterWithSpaces(filters.SearchFilter):
    def get_search_terms(self, request):
        params = request.query_params.get(self.search_param, '')
        terms =  params.split(",")
        return [term.strip() for term in terms]


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class QuestionsAPIView(generics.ListCreateAPIView):
    search_fields = ['pub_date', 'is_featured']
    filter_backends = (filters.SearchFilter,)
    # filter_backends = (DynamicSearchFilter,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
