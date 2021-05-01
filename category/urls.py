from django.urls import path

from category.views import CategoryListView, CategoryDetailView, TVShowListView, TVShowDetailListView, CommentListView
from category_user.views import UserListView, UserDetailView

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('show/', TVShowListView.as_view()),
    path('show/<int:pk>/', TVShowDetailListView.as_view()),
    path('show/', CommentListView.as_view()),
    path('user/', UserListView.as_view()),
    path('user/', UserDetailView.as_view())
]