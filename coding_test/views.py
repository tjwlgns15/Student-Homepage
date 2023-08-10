from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Codingsite


class coding_postingList(ListView):  # 모든 데이터를 확인 # 모든 데이터를 확인
    model = Codingsite
