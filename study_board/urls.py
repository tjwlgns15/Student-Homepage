from django.urls import path
from study_board import views

app_name = 'study_board'

urlpatterns = [
    path('',views.Study_BoardList.as_view(), name='study_board'),
    path('new/', views.Study_BoardCreate.as_view(), name='study_board_new'),
    path('edit/<int:pk>', views.Study_BoardUpdate.as_view(), name='study_board_edit'),
    path('delete/<int:pk>', views.Study_BoardDelete.as_view(), name='study_board_delete'),
    path('detail/<int:pk>', views.Study_BoardDetail.as_view(), name='study_board_detail'),
]