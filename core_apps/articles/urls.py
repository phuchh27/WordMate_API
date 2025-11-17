from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleListCreateView.as_view(), name="article-list-create"),
    path("<uuid:id>/", views.ArticleRetrieveUpdateDestroyView.as_view(),
         name="article-retrieve-update-destroy"),
]
