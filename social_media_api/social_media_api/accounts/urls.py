from django.urls import path
from . import views
from .views import FollowView, UnfollowView

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('follow/<int:user_id>/', FollowView.as_view()),
    path('unfollow/<int:user_id>/', UnfollowView.as_view()),
]