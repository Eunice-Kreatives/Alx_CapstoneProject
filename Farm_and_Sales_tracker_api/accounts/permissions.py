from rest_framework import permissions # pyright: ignore[reportMissingImports]


class IsAdminOrFarmer(permissions.BasePermission):
        """
        Custom permission to only allow 'Admin' or 'Farmer' users to
        perform write operations (create, update, delete).
        'Customer' users will be implicitly denied write access
        when this is combined with other permissions like IsAuthenticated.
        """
        def has_permission(self, request, view):
            # Allow GET, HEAD, OPTIONS requests (read-only) for anyone authenticated
            if request.method in permissions.SAFE_METHODS:
                return request.user and request.user.is_authenticated

            # For write methods (POST, PUT, PATCH, DELETE),
            # only allow Admin or Farmer roles
            return request.user and request.user.is_authenticated and \
                   request.user.role in ['admin', 'farmer']

        def has_object_permission(self, request, view, obj):
            # Object-level permissions for write methods (e.g., a farmer can only edit their own product)
            # This will be handled more specifically in the ViewSets' get_queryset/perform_create/update.
            # For now, we defer to has_permission for write methods.
            # For read methods, any authenticated user (including customer) has object permission if they passed has_permission.
            if request.method in permissions.SAFE_METHODS:
                return True

            # For write methods, if has_permission passed, it means they are Admin/Farmer.
            # Further object-level checks (e.g., is owner) will be in the ViewSet.
            return True
    