import collections
from graphene import ObjectType, String, Schema, Int, Field, List
from polls.models import Question


Person = collections.namedtuple("Person", ['first_name', 'last_name', 'age'])
data = {
    1: Person("steve", "jobs", 56),
    2: Person("bill", "gates", 63),
    3: Person("ken", "thompson", 76),
    4: Person("guido", "rossum", 63)
}

class PersonType(ObjectType):
    family_name = String(title=String(default_value='raaj'))
    first_name = String()
    last_name = String()
    age = Int()

    def resolve_first_name(person, info):
        return person.first_name

    def resolve_last_name(person, info):
        return person.last_name

    def resolve_family_name(person, info, title):
        return title

    def resolve_age(person, info):
        return person.age


class Query(ObjectType):
    person = Field(PersonType, key=Int(default_value=1))
    people = List(PersonType, keys=List(Int, default_value=data.keys()))

    def resolve_person(root, info, key):
        return data[key]

    def resolve_people(root, info, keys):
        return [v for k, v in data.items() if k in keys]

schema = Schema(query=Query)
