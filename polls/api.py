from .models import Question, Choice

from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization


class QuestionResource(ModelResource):

    class Meta:
        # queryset = Question.objects.all()
        object_class = Question
        resource_name = 'questions'
        authorization = Authorization()
        # excludes = ('id',)

    def get_object_list(self, request):
        return Question.objects.filter(id__gt=71)


class ChoiceResource(ModelResource):

    question = fields.ForeignKey(QuestionResource, 'question', full=True)

    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choices'

class PersonResource(ModelResource):

    name = fields.CharField()
