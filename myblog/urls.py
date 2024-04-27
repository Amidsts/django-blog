from django.urls import path, include
from . import views


urlpatterns=[
    path("", views.home, name='home'),
    path("blog/", views.blog, name='blog'),
    path("posts/", views.blogPosts, name='create'),
    path("add_post/", views.addPost, name="add"),
    path("addrec/", views.addrec, name='addrec'),
    path("update/<int:id>/", views.updatePost, name='update'),
    path("delete/<int:id>/", views.deletePost, name='delete'),
    path("update/uprec/<int:id>/", views.uprec, name='uprec'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", views.authView, name='authView')
]