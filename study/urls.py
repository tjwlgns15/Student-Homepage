from django.urls import path
from . import views

app_name = 'study'

urlpatterns = [
    path('',views.studyList.as_view(), name='study'),
    path('new/', views.studyCreate.as_view(), name='studynew'),
    path('edit/<int:pk>', views.studyUpdate.as_view(), name='studyedit'),
    path('delete/<int:pk>', views.studyDelete.as_view(), name='studydelete'),
    path('detail/<int:pk>', views.studyDetail.as_view(), name='studydetail'),
    path('apply_study/', views.apply_study, name='apply_study')
]
