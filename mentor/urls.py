from mentor import views
from django.urls import include, path


urlpatterns = [
    path('', views.userprofile, name='nexus'),
    path('profile/', views.useroverview, name='profile'),
    path('mentors/', views.suggestions, name='mentor'),
    path('follow/<str:pk>', views.follow_request, name='follow_request'),
    path('unfollow/<str:pk>', views.unfollow_request, name='unfollow_request'),
    path('update/', views.accountupdate, name='profile_update'),
    path('profile/<str:pk>', views.profileview, name='profileview'),
    path('post/', views.post, name='post'),
    path('post/all', views.post_all, name='post_all'),
    path('post/new', views.create_post, name='create'),
    path('post/like', views.post_like, name='like'),
    path('post/unlike', views.post_unlike, name='unlike'),
    path('post/comment/<str:pk>', views.post_comment, name='comment'),
]