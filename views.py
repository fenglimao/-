from django.shortcuts import render
# Create your views here.


def showinfom(request):
    return render(request,"index.html")