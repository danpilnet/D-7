from django.urls import path
from .views import PostDetail, PostList, PostFilter, PostCreate, PostUpdate, PostDelete



urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>/', PostDetail.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]

