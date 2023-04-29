from django.shortcuts import render

# Create your views here.
def filter(request):
    d={'data':'HELLOW hI hOW Are You'}
    return render(request,'filter.html',d)