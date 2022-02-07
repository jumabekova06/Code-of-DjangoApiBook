
# posts/permissions.py
from rest_framework import permissions
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
# Разрешения только для чтения разрешены для любого запроса
        if request.method in permissions.SAFE_METHODS:
            return True
# Права на запись разрешены только автору поста
        return obj.author == request.user