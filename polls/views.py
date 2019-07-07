from rest_framework import generics
from rest_framework import filters


class QuestionsAPIView(generics.ListCreateAPIView):
    search_fields = ['question_text']
    filter_backends = (filters.SearchFilter,)
