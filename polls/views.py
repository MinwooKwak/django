from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question
from django.http import Http404

# Create your views here.
def index(request) :
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context, request))

    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

def detail(request, question_id) :
    #question
   # try :
        question = Question.objects.get(pk=question_id)
   # except Question.DoesNotExist:
     #   raise Http404("Question does not exist")
   #return HttpResponse("You're looking at question %s." % question_id)
   return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id) :
    return HttpResponse("You're looking at results %s." % question_id)

def vote(request, question_id) :
    return HttpResponse("You're voting on question %s." % question_id)