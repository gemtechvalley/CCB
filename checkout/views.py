from django.shortcuts import render


#from .models import Question
def index(request):
    context = {}
    return render(request, 'checkout/index.html', context)
