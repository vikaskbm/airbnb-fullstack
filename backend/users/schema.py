import graphene

from .types import UserType
from .mutations import CreateAccountMutation, LoginMutation
from .queries import resolve_user


class Query:
    user = graphene.Field(UserType, id=graphene.Int(), resolver=resolve_user)

class Mutation:
    create_account = CreateAccountMutation.Field()
    login = LoginMutation.Field()