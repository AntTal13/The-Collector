from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('stones/', views.stones_index, name='index'),
  path('stones/<int:stone_id>/', views.stones_detail, name='detail'),
  path('stones/create/', views.StoneCreate.as_view(), name='stones_create'),
  path('stones/<int:pk>/update/', views.StoneUpdate.as_view(), name='stones_update'),
  path('stones/<int:pk>/delete/', views.StoneDelete.as_view(), name='stones_delete'),
]