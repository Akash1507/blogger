from django.urls import path
from .views import (
    createPost,updatePost,deletePost,listPost,detailPost
)

urlpatterns = [
    path('', listPost),
    path('post/<str:postUrl>/', detailPost),
    path('post/<str:postUrl>/edit/',updatePost),
    path('post/<str:postUrl>/delete/', deletePost),
]
