from django.urls import path

from rest_framework.routers import SimpleRouter

from . import apiviews

app_name = 'polls'
urlpatterns = [
    path('questions/', apiviews.QuestionsView.as_view(), name='questions_view'),
    path('questions/<int:question_id>/', apiviews.QuestionDetailView.as_view(), name='question_detail_view'),
    path('questions/<int:question_id>/choices/', apiviews.QuestionChoicesView.as_view(), name='choices_view'),
    path('questions/<int:question_id>/vote/', apiviews.VoteView.as_view(), name='vote_view'),
    path('questions/<int:question_id>/result/', apiviews.QuestionResultView.as_view(), name='question_result_view'),

    path('choices/', apiviews.ChoicesView.as_view(), name='choices_view'),

    path('another-questions/', apiviews.AnotherQuestionsView.as_view({'get': 'list'}), name='another_questions_view'),
    path('another-questions/<int:question_id>/', apiviews.AnotherQuestionsView.as_view({'get': 'retrieve'}), name='another_questions_view_retreive'),
]

# Multiple viewsets can be registered with a single router.
# Each viewset will probably have actions list, create, retrieve, partial_update, destroy.
router = SimpleRouter()
router.register('yet-another-questions', apiviews.YetAnotherQuestionsViewSet, basename='yet-another-question')

urlpatterns += router.urls
