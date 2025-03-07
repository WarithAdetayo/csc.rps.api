from django.urls import path

from api.result_processing.level.views import LevelListCreateView, LevelDetailView

urlpatterns = [
    path('', LevelListCreateView.as_view(), name='level-list-create'),
    path('<str:level_id>/', LevelDetailView.as_view(), name='level-detail'),
]
