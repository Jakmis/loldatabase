from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('champions/', views.ChampionListView.as_view(), name='champions'),
    path('champions/<int:pk>', views.ChampionDetailView.as_view(), name='champions_detail'),
]