from django.shortcuts import render


#from .models import Question
def index(request):
    context = {}
    return render(request, 'account/index.html', context)
