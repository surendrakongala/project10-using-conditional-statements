from django.shortcuts import render

# Create your views here.
def condition(request):
    dict={'a':10,'b':20,'c':30}
    return render(request,'condition.html',context=dict)