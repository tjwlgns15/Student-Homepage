from django.shortcuts import render
from .models import Certification
from .forms import CertificationForm

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator






# Sungjuk.object.all()
class Job_postingList(ListView):  # 모든 데이터를 확인
    model = Certification

class Job_postingDetail(DetailView):  # 생성자가 pk를 받음
    model = Certification  # 기본 형태
    fields = ['company_name', 'contents', 'exam_date', 'd_day']
    template_name = 'job_posting/detail.html'
    context_object_name = 'job_posting'  # 실제 데이터를 담았을 때의 이름


class Job_postingCreate(CreateView):
    model = Certification
    form_class = CertificationForm
    success_url = reverse_lazy('job_posting:job_posting')  # 입력을 성공하면 전체 데이터를 보여줌


def is_superuser(user):  # superuser 확인
    return user.is_superuser
class Job_postingUpdate(UpdateView):
    model = Certification
    form_class = CertificationForm
    success_url = reverse_lazy('job_posting:job_posting')

    @method_decorator(user_passes_test(is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class Job_postingDelete(DeleteView):
    model = Certification
    success_url = reverse_lazy('job_posting:job_posting')
    template_name = 'job_posting/certification_confirm_delete.html'

    @method_decorator(user_passes_test(is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
