import collections
from graphene import ObjectType, String, Schema, Int, Field, List


Person = collections.namedtuple("Person", ['first_name', 'last_name', 'age'])
data = {
    1: Person("akshar", "raaj", 30),
    2: Person("neelima", "gupta", 30),
    3: Person("shabda", "raaj", 35),
    4: Person("apaar", "raaj", 1)
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
