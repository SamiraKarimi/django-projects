from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    print(f'*'*50)
    # request.session is the cookies and it acts like a dictionary
    # request.session = {

    # }
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
         request.session['counter'] +=1

    randome=get_random_string(length=14)
    context = {
        'randome':randome
    }
    print(randome)
   
    return render(request,'index.html',context)  
def generate(request):
    return redirect('/')
def reset(request):
     request.session.clear()
     return redirect('/')
