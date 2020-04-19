from django.shortcuts import render,redirect
import random, datetime


def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold']=0
    if 'activities' not in request.session:
        request.session['activities']=[]
    return render(request,'index.html')
def process(request):
    print(f"*"*50)
    print(request.POST['location'])
    if request.POST['location'] =='farm':
        earned=random.randrange(10,21)
        request.session['total_gold'] += earned
        x = datetime.datetime.now()
        yourAc = f"You earned {earned} gold in farm ({x})" 
        request.session['activities'].append(yourAc)

    elif request.POST['location'] == 'cave':
        earned = random.randrange(5,11)
        request.session['total_gold'] +=earned 
        x = datetime.datetime.now()
        yourAc = f"You earned {earned} gold in cave ({x})" 
        request.session['activities'].append(yourAc)

    elif request.POST['location'] == 'house':
        earned = random.randrange(2,6)
        print(earned)
        request.session['total_gold'] +=earned 
        x = datetime.datetime.now()
        yourAc = f"You earned {earned} gold in House ({x})" 
        request.session['activities'].append(yourAc)

    elif request.POST['location'] =='casino':
        earned=random.randrange(-51,51)
        request.session['total_gold'] +=earned
        x = datetime.datetime.now()
        if earned>=0:
            yourAc = f"You earned {earned} gold in casino ({x})" 
        else: 
            yourAc = f"Entered a casino and lost {earned} gold...Oouch ({x})"

        request.session['activities'].append(yourAc)
    return redirect('/') 
def reset(request):
    request.session.clear()
    return redirect('/') 