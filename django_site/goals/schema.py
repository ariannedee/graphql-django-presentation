import django_filters
import graphene
from django.contrib.auth.models import User
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from goals.models import KeyResult, Objective


class KeyResultNode(DjangoObjectType):
    class Meta:
        model = KeyResult
        interfaces = (relay.Node,)


class ObjectiveNode(DjangoObjectType):
    progress = graphene.Int()

    class Meta:
        model = Objective
        interfaces = (relay.Node,)
        filter_fields = ['name']


class OwnerNode(DjangoObjectType):
    full_name = graphene.String()

    @graphene.resolve_only_args
    def resolve_full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    class Meta:
        interfaces = (relay.Node,)
        model = User


class ObjectiveFilter(django_filters.FilterSet):
    # Do case-insensitive lookups on 'name'
    name = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Objective
        fields = ['name']


class Query(graphene.ObjectType):
    objectives = DjangoFilterConnectionField(ObjectiveNode, filterset_class=ObjectiveFilter)
    users = DjangoFilterConnectionField(OwnerNode)


schema = graphene.Schema(
    query=Query
)