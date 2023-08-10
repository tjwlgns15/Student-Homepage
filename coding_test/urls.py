from django.contrib import admin
from django.urls import path, include
from job_posting import views
from coding_test import views

app_name = 'coding_test'

urlpatterns = [
    path('', views.coding_postingList.as_view(), name='coding_test'),

]

