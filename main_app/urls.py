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
  path('stones/<int:stone_id>/add_use/', views.add_use, name='add_use'),
  path('stones/<int:stone_id>/assoc_villain/<int:villain_id>/', views.assoc_villain, name='assoc_villain'),
  path('stones/<int:stone_id>/unassoc_villain/<int:villain_id>/', views.unassoc_villain, name='unassoc_villain'),
  path('villains/', views.VillainList.as_view(), name='villains_index'),
  path('villains/<int:pk>/', views.VillainDetail.as_view(), name='villains_detail'),
  path('villains/create/', views.VillainCreate.as_view(), name='villains_create'),
  path('villains/<int:pk>/update/', views.VillainUpdate.as_view(), name='villains_update'),
  path('villains/<int:pk>/delete/', views.VillainDelete.as_view(), name='villains_delete'),
]