from rest_framework.permissions import BasePermission
from . import models


class IsMe(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.email == 'asd@gmail.com'
        )

    def has_object_permission(self, request, view, obj: models.Product):
        return request.user == obj.user
