from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View
class Home(View):
    def get(self,request):
        return render(request,'input.html')
class Add(View):
    def get(self,request):
        x = request.GET["t1"]
        y = request.GET["t2"]
        op = request.GET["operation"]
        if op=="add":
            i=int(x)
            j=int(y)
            k=i+j
            res=HttpResponse("the sum is:"+str(k))
            return res
        elif op=="sub":
            i = int(x)
            j = int(y)
            k = i - j
            res = HttpResponse("the sub is:" + str(k))
            return res
        elif op=="mul":
            i = int(x)
            j = int(y)
            k = i * j
            res = HttpResponse("the mul is:" + str(k))
            return res
        else:
            i = int(x)
            j = int(y)
            k = i / j
            res = HttpResponse("the div is:" + str(k))
            return res