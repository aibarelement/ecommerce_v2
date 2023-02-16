from rest_framework.permissions import BasePermission

from users import choices as user_choices


class IsCustomer(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.user_type == user_choices.UserTypeChoices.Customer
        )
