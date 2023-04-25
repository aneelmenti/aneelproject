from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')
def add(request):
    a=request.GET["t1"]
    b=request.GET["t2"]
    i=int(a)
    j=int(b)
    k=i+j
    res=HttpResponse("the sum is:"+str(k))
    return res

