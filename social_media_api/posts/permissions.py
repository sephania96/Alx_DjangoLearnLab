from django.db.models import Q
from rest_framework import viewsets, permissions
from .models import Post, Follow
from .serializers import PostSerializer
from .pagination import StandardResultsSetPagination

class IsFollowing(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

