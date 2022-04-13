import graphene
from graphene_django import DjangoObjectType
from .models import Profile, Photos, Contacts


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"


class PhotoType(DjangoObjectType):
    class Meta:
        model = Photos
        fields = "__all__"


class ContactsType(DjangoObjectType):
    class Meta:
        model = Contacts
        fields = "__all__"


class Query(graphene.ObjectType):
    all_profiles = graphene.List(ProfileType)
    all_photo = graphene.List(PhotoType)
    all_contacts = graphene.List(ContactsType)

    def resolve_all_profiles(root, info):
        return Profile.objects.all()

    def resolve_all_photos(root, info):
        return Photos.object.all()

    def resolve_all_Contacts(root, info):
        return Contacts.objects.all()
