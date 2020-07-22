from rest_framework import permissions



class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True


        # Write permissions are only allowed to the author of a post
        return obj.author == request.user

'''
         We do not need else here.

         else:
            return obj.author == request.user

        eta likhle logic e problem hoy

        ei function e jekono request er jonno return obj.author == request.user
        check kora hobe.....tobe jodi request get type hoy tahole always TRUE hobe

'''
