from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.


def t2(reqest):
    return render_to_response("./myweb/test.html")

def t(request):
    return HttpResponse("Hello world")
