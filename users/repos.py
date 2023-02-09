from typing import Protocol, OrderedDict

from rest_framework.generics import get_object_or_404

from . import models


class UserReposInterface(Protocol):

    @staticmethod
    def create_user(data: OrderedDict) -> models.User: ...

    @staticmethod
    def get_user(data: OrderedDict) -> models.User: ...


class UserReposV1:

    @staticmethod
    def create_user(data: OrderedDict) -> models.User:
        return models.User.objects.create_user(**data)

    @staticmethod
    def get_user(data: OrderedDict) -> models.User:
        return get_object_or_404(models.User, **data)
