import datetime
from graphene import Schema, ObjectType, Field, String, List, Int, Mutation

from polls.models import Question, Choice


class ChoiceType(ObjectType):
    choice_text = String()
    votes = Int()

    def resolve_choice_text(choice, info):
        return choice.choice_text

    def resolve_votes(choice, info):
        return choice.votes

class QuestionType(ObjectType):

    question_text = String()
    pub_date = String()
    ID = Int()
    choices = List(ChoiceType)

    def resolve_question_text(question, info):
        return question.question_text

    def resolve_pub_date(question, info):
        return question.pub_date.strftime('%Y-%m-%d')

    def resolve_ID(question, info):
        return question.id

    def resolve_choices(question, info):
        return question.choice_set.all()


class CreateChoice(Mutation):
    class Arguments:
        question_id = Int()
        choice_text = String()

    choice = Field(ChoiceType)

    def mutate(root, info, question_id, choice_text):
        question = Question.objects.get(id=question_id)
        choice = Choice.objects.create(question=question, choice_text=choice_text)
        return CreateChoice(choice)
    

class CreateQuestion(Mutation):
    class Arguments:
        question_text = String()
        pub_date = String()

    question = Field(QuestionType)

    def mutate(root, info, question_text, pub_date):
        pub_date = datetime.datetime.strptime(pub_date, '%Y-%m-%d')
        question = Question.objects.create(question_text=question_text, pub_date=pub_date)
        return CreateQuestion(question=question)


class MyMutations(ObjectType):
    create_question = CreateQuestion.Field()
    create_choice = CreateChoice.Field()


class Query(ObjectType):
    questions = List(QuestionType)
    question = Field(QuestionType, id=Int())

    def resolve_questions(root, info):
        return Question.objects.all()

    def resolve_question(root, info, id):
        return Question.objects.get(id=id)


schema = Schema(query=Query, mutation=MyMutations)
