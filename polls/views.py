from django.views import View
from django.http import JsonResponse

from rest_framework import generics
from rest_framework import filters

from .models import Question
from .serializers import QuestionSerializer
from .graphene import schema
# from hello_graphene import schema


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


class GraphQLView(View):
    """
    TODO:
    1. Question list
    2. Question detail
    3. Choice list
    4. Choice detail
    5. Question along with all choices
    6. Filter on question_text

    ADVANCED
    1. Filter on question choices. Don't get all the choices for a particular question
    1. Want a page which shows all admin users under one section and staff users under another section
    """

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        result = schema.execute(search)
        return JsonResponse(result.data, safe=False)
