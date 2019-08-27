from django.urls import path

from rest_framework.routers import SimpleRouter

from . import apiviews
from . import views

app_name = 'polls'
urlpatterns = [
    path('choices/', apiviews.ChoicesView.as_view(), name='choices_view'),
    path('questions/', views.QuestionsAPIView.as_view()),
    path('graphql/', views.GraphQLView.as_view())
]

# Multiple viewsets can be registered with a single router.
# Each viewset will probably have actions list, create, retrieve, partial_update, destroy.
router = SimpleRouter()
router.register('questions', apiviews.QuestionsViewSet, basename='question')

urlpatterns += router.urls
