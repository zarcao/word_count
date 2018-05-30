from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Question



#from django.conf import settings
# Create your views here.


def index(request):
    q_list = Question.objects.all()
    context = {
        'q_list':q_list,
    }
    return render(request,'polls/index.html',context)

def ins_question(request):
    return render(request,'polls/ins.html')

def counts(request):
    a_text = request.GET['text']
    a_len = len(a_text)

    word_dict = {}
    for word in a_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    word_dict_sort = sorted(word_dict.items(),key=lambda x:x[1],reverse=True)

    context = {
        'a_text':a_text,
        'a_len':a_len,
        'a_word':word_dict_sort
    }
    return render(request,'polls/counts.html',context)


def question_list(request):
    q_list = Question.objects.filter(id = '1')
    context = {
        'q_list':q_list,
    }
    print(q_list)
    return render(request,'polls/q_list.html',context)


def detail(request, question_id):
    q_list = get_object_or_404(Question,id=question_id)
    return render(request,'polls/detail.html',{'q_list':q_list})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def page_not_found(request):
    return render(request,'polls/404.html')
def page_server_error(request):
    return render(request,'polls/500.html')