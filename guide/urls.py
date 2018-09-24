from django.urls import path

from . import views

app_name = 'guide'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('category/restaurants/', views.category_restaurants, name='restaurants'),
    path('category/restaurants/<str:handle>/', views.category_restaurants_detail, name='restaurant'),
    path('category/<str:handle>/', views.category_restaurants, name='category'),
    path('map/', views.map, name='map'),
    path('search/', views.search, name='search'),
]