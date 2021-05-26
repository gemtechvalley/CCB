from django.shortcuts import render

#from .models import Question
def index(request):
    context = {}
    return render(request, 'sale/index.html', context)
