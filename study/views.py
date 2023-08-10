from django.shortcuts import render, redirect
from .models import study
from .forms import studyForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

class studyList(ListView):
    model = study

class studyCreate(CreateView):
    model = study
    form_class = studyForm
    success_url = reverse_lazy('study:study')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class studyUpdate(UpdateView):
    model = study
    fields = ['title', 'content']
    success_url = reverse_lazy('study:study')

class studyDelete(DeleteView):
    model = study
    success_url = reverse_lazy('study:study')
    template_name = 'study/study_delete.html'

@login_required(login_url='/account/login/')
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user

        post = study(title=title, content=content, user=user)
        post.save()

        messages.success(request, '게시글이 작성되었습니다.')
        return redirect('studylist')

    return render(request, 'study')

class studyDetail(DetailView):
    model = study
    fields = ['title', 'content', 'date']
    template_name = 'study/study_detail.html'
    context_object_name = 'study'

def apply_study(request):
    if request.method == 'POST':
        study_id = request.POST.get('study_id')
        study_obj = get_object_or_404(study, id=study_id)
        study_obj.people += 1
        study_obj.save()
        return JsonResponse({'success': True, 'updated_people': study_obj.people})
    else:
        return JsonResponse({'success': False})