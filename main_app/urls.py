from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>', views.records_detail, name='detail'),
    path('records/create', views.RecordCreate.as_view(), name='records_create'),
    path('records/<int:pk>/update', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete', views.RecordDelete.as_view(), name='records_delete'),
    path('records/<int:record_id>/add_market/', views.add_market, name='add_market'),
    path('records/<int:record_id>/assoc_genre/<int:genre_id>/', views.assoc_genre, name='assoc_genre'),
    path('genres/', views.GenreList.as_view(), name='genres_index'),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name='genres_detail'),
    path('genres/create/', views.GenreCreate.as_view(), name='genres_create'),
    path('genres/<int:pk>/update/', views.GenreUpdate.as_view(), name='genres_update'),
    path('genres/<int:pk>/delete/', views.GenreDelete.as_view(), name='genres_delete'),
]