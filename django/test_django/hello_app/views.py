from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    text = "<h1>My name is Urvi</h1> "
    return HttpResponse(text)