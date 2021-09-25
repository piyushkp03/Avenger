from random import randint

from django.shortcuts import render,HttpResponse
from .models import datas

def home(request):
    error=""

    return render(request, 'home.html',{'error':error})
def know(request):
    
    name = request.POST['uname']
    age=request.POST['uage']
    gender=request.POST['ugender']
    print(name,type(name),age,type(age),gender)
    error="Please enter both Name and age!"
    if age=="" or name=="":
        return render(request,"home.html",{"error":error})
    age=int(age)
    
    dataas1 = datas()
    dataas2 = datas()
    dataas3 = datas()
    dataas4 = datas()
    dataas5 = datas()
    dataas6 = datas()
    dataas7 = datas()
    dataas8 = datas()
    dataas9 = datas()
    dataas10 = datas()
    dataas11 = datas()
    dataas12 = datas()
    
    dataas1.img = 'static/scarlet.jpg'
    dataas2.img = 'static/valkayre.jpg'
    dataas3.img = 'static/capmarvel.jpg'
    dataas4.img = 'static/black.jpg'
    dataas5.img = 'static/iron.jpg'
    dataas6.img ='static/thor.jpg'
    dataas7.img = 'static/vision.jpg'
    dataas8.img='static/hulk.jpg'
    dataas9.img = 'static/hawk.jpg'
    dataas10.img='static/spider.jpg'
    #dataas.img = 'static/blackpanther.jpg'
    dataas11.img='static/cap.jpg'
    dataas12.img = 'static/dr.jpg'
   
    
    #dataas8.img = 'static/bheem.jpg'
    #dataas9.img = 'static/thor.jpg'
    #dataas10.img = 'static/iron.jpg'
    #dataas11.img = 'static/cap.jpg'

    dataas1.uname=name
    dataas2.uname = name
    dataas3.uname = name
    dataas4.uname = name
    dataas5.uname = name
    dataas6.uname = name
    dataas7.uname = name
    dataas8.uname = name
    dataas9.uname = name
    dataas10.uname = name
    dataas11.uname = name
  

    #dataas1.match =" OMNIPOTENT ,OMNISCIENT AND SHIVA HIMSELF,LORD KRISHNA!!!"
    dataas1.match="LADY WITH SUPERNATURAL POWERS, SCARLET WITCH!!"
    dataas2.match = "EXCELLENT FIGHTER AND WARRIORESS, VALKYRIE!! "
    dataas3.match = "MOST POWERFUL SUPERWOMAN WITH IMMENSE STRENGTH!!!"
    dataas4.match = "VERY FAST AND BEST IN HAND TO HAND COMBAT, BLACK WIDOW!!"
    dataas5.match = "INVINCIBLE AND ROCK,IRON MAN!!!"
    dataas6.match =  "LORD OF THUNDER, THOR!!!"
   # dataas7.match = " OMNIPOTENT ,OMNISCIENT AND SHIVA HIMSELF,LORD KRISHNA!!!"
    dataas8.match = "PHYSICALLY STRONGEST OF ALL, HULK!!!"
    dataas9.match = "EXCELLENT ARCHER ,HAWK!!"
    dataas10.match = "GENIUS LEVEL INTELLECT WITH SUPERB SPEED AND DURABILITY, SPIDERMAN!!!"
    dataas7.match = "POWER OF THOR AND IRONMAN,VISION!!!"
    dataas11.match = "AVENGERS' CAPTAIN AND LEADER,CAPTAIN AMERICA !!!"


    fdataas=[dataas1, dataas2, dataas3, dataas4]
    mdataas=[dataas5,dataas6, dataas7, dataas8, dataas9, dataas10, dataas11]
    x=randint(0, 10)
    if gender=='female':
        if age%4==0:
          return render(request, 'page2.html', {'dataas': fdataas[0],'age':age})
        elif age%4==1:
          return render(request, 'page2.html', {'dataas': fdataas[1],'age':age})
        elif age%4==2:
          return render(request, 'page2.html', {'dataas': fdataas[2],'age':age})
        else:
          return render(request, 'page2.html', {'dataas': fdataas[3],'age':age})
        
    else:
        if age%7==1:
          return render(request, 'page2.html', {'dataas': mdataas[0],'age':age})
        elif age%7==2:
          return render(request, 'page2.html', {'dataas': mdataas[1],'age':age})
        elif age%7==3:
          return render(request, 'page2.html', {'dataas': mdataas[2],'age':age})
        elif age%7==4:
          return render(request, 'page2.html', {'dataas': mdataas[3],'age':age})
        elif age%7==5:
          return render(request, 'page2.html', {'dataas': mdataas[4],'age':age})
        elif age%7==6:
          return render(request, 'page2.html', {'dataas': mdataas[5],'age':age})
        else:
          return render(request, 'page2.html', {'dataas': mdataas[6],'age':age})
      
