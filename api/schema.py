import graphene
from users.query import Query as UsersQuery
from follows.query import Query as FollowsQuery
#from posts.query import Query as PostsQuery
from profiles.query import Query as ProfilesQuery


class Query(ProfilesQuery, UsersQuery, FollowsQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hello world!")


schema = graphene.Schema(query=Query)
