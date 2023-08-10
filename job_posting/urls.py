from django.contrib import admin
from django.urls import path, include
from job_posting import views

app_name = 'job_posting'

urlpatterns = [
    path('', views.Job_postingList.as_view(), name='job_posting'),
    path('detail/<int:pk>', views.Job_postingDetail.as_view(), name='detail'),  # 추가
    path('new/', views.Job_postingCreate.as_view(), name='job_posting_new'),
    path('edit/<int:pk>', views.Job_postingUpdate.as_view(), name='job_posting_edit'),
    path('delete/<int:pk>', views.Job_postingDelete.as_view(), name='job_posting_delete'),
]

