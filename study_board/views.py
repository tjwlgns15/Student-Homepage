from django.shortcuts import render,redirect
from .models import Study_Board
from .forms import Study_BoardForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404


class Study_BoardList(ListView):
    model = Study_Board


class Study_BoardCreate(CreateView):
    model = Study_Board
    form_class = Study_BoardForm
    success_url = reverse_lazy('study_board:study_board')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Study_BoardUpdate(UpdateView):
    model = Study_Board
    fields = ['title', 'content']
    success_url = reverse_lazy('study_board:study_board')

class Study_BoardDelete(DeleteView):
    model = Study_Board
    success_url = reverse_lazy('study_board:study_board')
    template_name = 'study_board/study_board_delete.html'

@login_required(login_url='/account/login/')
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user # 현재 로그인한 유저 정보를 가져옴

        post = Study_Board(title=title, content=content, user=user)
        post.save()

        messages.success(request, '게시글이 작성되었습니다.')
        return redirect('study_board_list')

    return render(request, 'study_board')

class Study_BoardDetail(DetailView):
    model = Study_Board
    fields = ['title', 'content', 'date']
    template_name = 'study_board/study_board_detail.html'
    context_object_name = 'study_board'

