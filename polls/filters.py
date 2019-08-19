import django_filters

from .models import Question

class QuestionFilter(django_filters.FilterSet):

    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
