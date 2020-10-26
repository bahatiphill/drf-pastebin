from rest_framework import permissions

class IsOwnerOrReadyOnly(permissions.BasePermission):
    """
    Custom permissions to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # So we will always allow GET, HEAD or OPTIONS request.

        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet
        return obj.owser == request.user
        