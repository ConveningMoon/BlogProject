from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('api/v1/', include('blog.api_urls')),  # Add this line
]
