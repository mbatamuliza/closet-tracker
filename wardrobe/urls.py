from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import signup_view

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.ClothingItemList.as_view(), name='clothingitem_list'),
    path('item/<int:pk>/', views.ClothingItemDetail.as_view(), name='clothingitem_detail'),
    path('items/create/', views.ClothingItemCreate.as_view(), name='clothingitem_create'),
    path('items/<int:pk>/update/', views.ClothingItemUpdate.as_view(), name='clothingitem_update'),
    path('items/<int:pk>/delete/', views.ClothingItemDelete.as_view(), name='clothingitem_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
]