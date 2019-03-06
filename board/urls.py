from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('create/', views.board_create, name="board_create"),
    path('<int:pk>/', views.board_view, name="board_view"),
    path('delete/<int:pk>/', views.board_delete, name="board_delete"),
    path('check/', views.check_password, name="check_password"),
    path('update/<int:pk>/', views.board_update, name="board_update"),
]
