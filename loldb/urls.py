from django.urls import  path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('champions/', views.ChampionListView.as_view(), name='champions'),
    path('champions/<int:pk>', views.ChampionDetailView.as_view(), name='champions_detail'),
    path('regions/', views.RegionListView.as_view(), name='regions'),
    path('regions/<int:pk>', views.RegionDetailView.as_view(), name='regions_detail'),
]