from django.urls import path
from . import views

urlpatterns = [
    # restaurant urls
    path('', views.index, name='app-home'),
    path('app/restaurants/', views.RestaurantListView.as_view(),
         name='app-restaurant-list'),
    path('restaurants/<int:pk>/', views.ResturantDetailView.as_view(),
         name='app-restaurant-detail'),
    path('app/restaurants/create/',
         views.restaurants_create, name='app-restaurant-create'),
    path('app/restaurants/edit/<int:pk>/',
         views.restaurants_edit, name='app-restaurant-edit'),
    path('app/restaurants/delete/<int:pk>/',
         views.restaurants_delete, name='app-restaurant-delete'),
    path('app/restaurants/<int:fk>/menu-itens/create/',
         views.menu_itens_create, name='app-menu-item-create'),
    path('app/restaurants/<int:fk>/menu-itens/edit/<int:pk>/',
         views.menu_itens_edit, name='app-menu-item-edit'),
    path('app/restaurants/<int:fk>/menu-itens/delete/<int:pk>/',
         views.menu_itens_delete, name='app-menu-item-delete'),
]
