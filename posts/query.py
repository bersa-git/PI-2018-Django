import graphene
from graphene_django import DjangoObjectType

from .models import Post, PostPhotos


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("__all__",)


class PostPhotoType(DjangoObjectType):
    class Meta:
        model = PostPhotos
        fields = ("__all__",)


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    all_post_photos = graphene.List(PostPhotoType)

    def resolve_all_posts(root, info):

        return Post.objects.all()

    def resolve_all_post_photos(root, info):

        return Post.objects.all()

