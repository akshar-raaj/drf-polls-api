from django.urls import path, include

from rest_framework.routers import SimpleRouter

from . import apiviews
from . import api
from tastypie.api import Api

app_name = 'polls'
urlpatterns = [
    path('choices/', apiviews.ChoicesView.as_view(), name='choices_view'),
]

# Multiple viewsets can be registered with a single router.
# Each viewset will probably have actions list, create, retrieve, partial_update, destroy.
router = SimpleRouter()
router.register('questions', apiviews.QuestionsViewSet, basename='question')

urlpatterns += router.urls

question_resource = api.QuestionResource()
choice_resource = api.ChoiceResource()

v1_api = Api(api_name='v1')
v1_api.register(api.QuestionResource())
v1_api.register(api.ChoiceResource())

tastypie_patterns = [
    path(r'tastypie/', include(question_resource.urls)),
    path(r'tastypie/', include(choice_resource.urls)),
    path(r'api/', include(v1_api.urls)),
]

urlpatterns += tastypie_patterns
