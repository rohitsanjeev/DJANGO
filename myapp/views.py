from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("welcome to myapp")

#simple view code
#create a urls.py inside your app i.e (myapp)

