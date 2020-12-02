from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views import generic
from django.utils import timezone


from .models import Question, Choice


# Create your views here.
def index(request):

    return render(request, 'polls/index.html')

def detail(request):

    return render(request, 'polls/detail.html')
def cv(request):
    return render(request, 'polls/cv.html')
def contact(request):
    return render(request, 'polls/contact.html')
