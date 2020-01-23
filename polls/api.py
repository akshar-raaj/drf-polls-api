from .models import Question, Choice

from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization


class ChoiceResource(ModelResource):

    question_text_lower = fields.CharField(attribute='question__question_text_lower')

    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choices'


class QuestionResource(ModelResource):

    question_text_duplicate = fields.CharField(attribute='question_text', readonly=True)

    class Meta:
        queryset = Question.objects.all()
        object_class = Question
        resource_name = 'questions'
        list_allowed_methods = ['get', 'post']
        authorization = Authorization()

    def dehydrate(self, bundle):
        bundle.data['len_question_text'] = len(bundle.data['question_text'])
        return bundle
