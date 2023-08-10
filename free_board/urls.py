from django.urls import path
from free_board import views

app_name = 'free_board'

urlpatterns = [
    path('',views.Free_BoardList.as_view(), name='free_board'),
    path('new/', views.Free_BoardCreate.as_view(), name='free_board_new'),
    path('edit/<int:pk>', views.Free_BoardUpdate.as_view(), name='free_board_edit'),
    path('delete/<int:pk>', views.Free_BoardDelete.as_view(), name='free_board_delete'),
    path('detail/<int:pk>', views.Free_BoardDetail.as_view(), name='free_board_detail'),
]