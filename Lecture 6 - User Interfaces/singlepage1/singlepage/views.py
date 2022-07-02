from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")
    
texts = ["Sample_text 1: Hello my name is Rookie",\
         "Sample_text 2: Greetings everyone!",\
         "Sample_text 3: Bye! it was nice meeting you!"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")