from django.shortcuts import render,redirect
from .models import Free_Board
from .forms import Free_BoardForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404


class Free_BoardList(ListView):
    model = Free_Board


class Free_BoardCreate(CreateView):
    model = Free_Board
    form_class = Free_BoardForm
    success_url = reverse_lazy('free_board:free_board')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Free_BoardUpdate(UpdateView):
    model = Free_Board
    fields = ['title', 'content']
    success_url = reverse_lazy('free_board:free_board')

class Free_BoardDelete(DeleteView):
    model = Free_Board
    success_url = reverse_lazy('free_board:free_board')
    template_name = 'free_board/free_board_delete.html'

@login_required(login_url='/account/login/')
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user # 현재 로그인한 유저 정보를 가져옴

        post = Free_Board(title=title, content=content, user=user)
        post.save()

        messages.success(request, '게시글이 작성되었습니다.')
        return redirect('free_board_list')

    return render(request, 'free_board')

class Free_BoardDetail(DetailView):
    model = Free_Board
    fields = ['title', 'content', 'date']
    template_name = 'free_board/free_board_detail.html'
    context_object_name = 'free_board'