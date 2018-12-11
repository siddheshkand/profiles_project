from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user can only update their own profile"""

        # Check if method of current user is safe i.e. GET method and not PUT, DELETE
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check & return that user can only modify his content only and not other user profile
        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow user to update own status"""

    def has_object_permission(self, request, view, obj):
        """Check user can only update their own profile"""

        # Check if method of current user is safe i.e. GET method and not PUT, DELETE
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check & return that user can only modify his content only and not other user profile
        return obj.user_profile.id == request.user.id
