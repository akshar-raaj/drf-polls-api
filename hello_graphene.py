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
    first_name = String()
    last_name = String()
    age = Int()
    friends = List('self')

    def resolve_first_name(person, info):
        return person.first_name

    def resolve_last_name(person, info):
        return person.last_name

    def resolve_age(person, info):
        return person.age


class Query(ObjectType):
    person = Field(PersonType)

    def resolve_person(root, info):
        # return Person("apaar", "raaj", 1)

        return data[1]


schema = Schema(query=Query)
