from graphene import ObjectType, String, Schema, Int, Field, List

from .models import Question


class Questions(ObjectType):
    question_text = String()
    pk = Int()

    def resolve_question_text(question, info):
        return question.question_text

    def resolve_pk(question, info):
        return question.pk


class Query(ObjectType):
    questions = List(Questions)

    def resolve_questions(root, info):
        return Question.objects.all()


schema = Schema(query=Query)
