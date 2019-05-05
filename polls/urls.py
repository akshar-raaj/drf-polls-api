from django.urls import path

from . import views
from . import apiviews

app_name = 'polls'
urlpatterns = [
    path('questions/', apiviews.QuestionsView.as_view(), name='questions_view'),
    path('questions/<int:question_id>/', apiviews.QuestionDetailView.as_view(), name='question_detail_view'),
    path('questions/<int:question_id>/choices/', apiviews.QuestionChoicesView.as_view(), name='choices_view'),
    path('questions/<int:question_id>/vote/', apiviews.VoteView.as_view(), name='vote_view'),
    path('questions/<int:question_id>/result/', apiviews.QuestionResultView.as_view(), name='question_result_view'),

    path('choices/', apiviews.ChoicesView.as_view(), name='choices_view'),
]
