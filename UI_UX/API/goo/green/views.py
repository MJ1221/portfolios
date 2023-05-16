from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question,Answer
from .forms import QuestionForm
import pandas as pd
from config import settings
import os

def data_coordinates():
    file_path = os.path.join(settings.STATIC_URL, 'data_jydo', 'all_map.txt')
    data = pd.read_csv(file_path, sep=',')
    j1 = []
    j2 = []
    j3 = []
    j4 = []
    url = []
    for index, row in data.iterrows():
        j1.append(row[0])
        j2.append(row[1])
        j3.append(row[2])
        j4.append(row[3])
        url.append(row[4])
    context = {'zip': zip(j1,j2,j3,j4,url)}
    return context

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('green:detail', question_id=question.id)

def question_create(request):
    form = QuestionForm()
    return render(request, 'green/question_form.html', {'form': form})

def start(request):
    return render(request, 'green/Initialize.html', {})


def home(request):
    return render(request, 'green/Jog.html', {})

def home1(request):
    return render(request, 'green/Spindle.html', {})

def home6(request):
    return render(request, 'green/Maintenance.html', {})

def home7(request):
    return render(request, 'green/Tool.html', {})


# Create your views here.
