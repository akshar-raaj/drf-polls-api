from graphene import Schema, ObjectType, Field, String, List, Int

from polls.models import Question


class QuestionType(ObjectType):

    question_text = String()
    pub_date = String()

    def resolve_question_text(question, info):
        return question.question_text

    def resolve_pub_date(question, info):
        return question.pub_date.strftime('%Y-%m-%d')


class Query(ObjectType):
    questions = List(QuestionType)
    question = Field(QuestionType, id=Int())

    def resolve_questions(root, info):
        return Question.objects.all()

    def resolve_question(root, info, id):
        return Question.objects.get(id=id)


schema = Schema(query=Query)
