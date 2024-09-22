from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .pagination import StandardResultsSetPagination
from .permissions import IsFollowing
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Notification

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class FollowingPostsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsFollowing]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(APIView):
    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            notification = Notification.objects.create(
                sender=user,
                receiver=post.author,
                post=post,
                notification_type='like'
            )
            serializer = LikeSerializer(like)
            return Response(serializer.data)
        return Response({'error': 'You already liked this post'})

class UnlikePostView(APIView):
    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        like = Like.objects.filter(post=post, user=user).first()
        if like:
            like.delete()
            notification = Notification.objects.filter(
                sender=user,
                receiver=post.author,
                post=post,
                notification_type='like'
            ).first()
            if notification:
                notification.delete()
            return Response({'message': 'Post unliked'})
        return Response({'error': 'You did not like this post'})