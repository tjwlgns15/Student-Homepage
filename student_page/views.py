from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
# from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect



class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

#건호

#윤호

#인호

#미정
