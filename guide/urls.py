from django.urls import path

from . import views



app_name = 'guide'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('category/synagogues/', views.category_synagogues, name='synagogues'),
    path('category/synagogues/<str:handle>/', views.category_synagogues_detail, name='synagogue'),
    path('category/restaurants/', views.category_restaurants, name='restaurants'),
    path('category/restaurants/<str:handle>/', views.category_restaurants_detail, name='restaurant'),
    path('map/', views.map, name='map'),
    path('search/', views.search, name='search'),
    path('api/restaurants', views.api_all_restaurants, name='api_all_restaurants'),
]