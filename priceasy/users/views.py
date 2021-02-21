from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Register(req):
    context ={}
    return render(req, 'users/base.html', context)
