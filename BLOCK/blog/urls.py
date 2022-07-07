from django.urls import path
from .views import ListObjectsView, DetailObjectsView, SearchResultsView, NeedUpdateView, PostDeleteView, PostCreateView

urlpatterns = [
    path('', ListObjectsView.as_view()),
    path('<int:pk>', DetailObjectsView.as_view(), name='detail'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('edit/<int:pk>', NeedUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('create/', PostCreateView.as_view(), name='create'),
]
