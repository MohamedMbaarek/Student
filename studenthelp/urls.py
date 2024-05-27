from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, TransportCreate, HousingNewsFeed, CreateHousingPost

app_name = 'studenthelp'  # Ajout de l'espace de noms de l'application

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('housing-news/', HousingNewsFeed.as_view(), name='housing_news_feed'),
    path('create-housing-post/', CreateHousingPost.as_view(), name='create_housing_post'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/create/', PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('transports/create/', TransportCreate.as_view(), name='transport_create'),
]
