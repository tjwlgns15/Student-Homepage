"""
URL configuration for student_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from student_page import views

urlpatterns = [
    # 지훈
    path("admin/", admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('job_posting/', include('job_posting.urls')),
    # 건호
    path('accounts/', include('accounts.urls')),
    path('study_board/', include('study_board.urls')),
    path('free_board/', include('free_board.urls')),
    # 미정
    path('coding_test/', include('coding_test.urls')),
    # 윤호
    path('study/', include('study.urls')),


]
