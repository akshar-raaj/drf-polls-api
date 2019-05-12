from django.urls import path

from rest_framework.routers import SimpleRouter

from . import apiviews

app_name = 'polls'
urlpatterns = [
    path('choices/', apiviews.ChoicesView.as_view(), name='choices_view'),
]

# Multiple viewsets can be registered with a single router.
# Each viewset will probably have actions list, create, retrieve, partial_update, destroy.
router = SimpleRouter()
router.register('questions', apiviews.QuestionsViewSet, basename='question')

urlpatterns += router.urls
