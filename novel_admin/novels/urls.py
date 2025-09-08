from django.urls import path
from .views import HomeView, LibraryView, NovelSearchView

urlpatterns=[
path('api/home/', HomeView.as_view(), name="home"),
path('api/library/', LibraryView.as_view(), name="library"),
path('api/novels/search/', NovelSearchView.as_view(), name="search"),
]