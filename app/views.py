from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':600,'b':2000,'c':500}
    return render(request,'conditional.html',d)

def looping(request):
    d={'name':'Bharath'}
    return render(request,'looping.html',d)