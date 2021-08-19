from django.shortcuts import render

# Create your views here.
def app(request):
    d={'a':'art'}
    return render(request,'loop.html',context=d)

    

    

