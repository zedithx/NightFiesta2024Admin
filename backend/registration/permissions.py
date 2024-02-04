from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """permission class that check if user is admin"""
    def has_permission(self, request, view):
        return request.user.is_staff
