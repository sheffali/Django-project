from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import forms
from . import models
#from fusioncharts import FusionCharts
from test1.forms import TestForm1
from test1.forms import Test5
from test1.forms import Test2
from test1.forms import Test3
from test1.forms import Test4
from test1.forms import Login
from test1.models import Regist
from test1.models import OTest
from test1.models import Test_r
from matplotlib import pylab
from pylab import *

def act1(request):
    tform= forms.Test2()
    print("hello")
    if request.method=='POST':
        tform=Test2(request.POST)
        if tform.is_valid():
            obj1=Test_r
            #tform.save(commit=False);
            i=1
            totscore=0
            ans1=tform['ans1'].value()
            ans2=tform['ans2'].value()
            ans3=tform['ans3'].value()
            ans4=tform['ans4'].value()
            ans5=tform['ans5'].value()
            ans6=tform['ans6'].value()
            ans7=tform['ans7'].value()
            ans8=tform['ans8'].value()
            ans9=tform['ans9'].value()
            ans10=tform['ans10'].value()
            obj1=tform.save(commit=False);

            if(ans1=='y'):
                totscore+=2
            if(ans2=='n'):
                totscore+=2
            if(ans3=='y'):
                totscore+=2
            if(ans4=='n'):
              totscore+=2
            if(ans5=='n'):
                totscore+=2
            if(ans6=='n'):
                totscore+=2
            if(ans7=='n'):
                totscore+=2
            if(ans8=='n'):
                totscore+=2
            if(ans9=='n'):
                totscore+=2
            if(ans10=='y'):
                totscore+=2
            totscore=int(totscore)
            obj1.type="calculation"
            obj1.Tscore=totscore
            obj1.save()
            return index2(request)
    return render(request,'test1/act1.html',context={'tform':tform})


def home(request):
    return render(request,'test1/home.html')




def act5(request):
    tform7= forms.Test5()
    print("hello")
    if request.method=='POST':
        tform7=Test5(request.POST)
        if tform7.is_valid():
            obj0=Test_r
            #tform.save(commit=False);
            totscore=0
            ans1=tform7['ans1'].value()
            ans2=tform7['ans2'].value()
            ans3=tform7['ans3'].value()
            ans4=tform7['ans4'].value()
            ans5=tform7['ans5'].value()
            ans6=tform7['ans6'].value()
            ans7=tform7['ans7'].value()
            ans8=tform7['ans8'].value()
            ans9=tform7['ans9'].value()
            ans10=tform7['ans10'].value()


            obj0=tform7.save(commit=False);

            if(ans1=='5'):
                totscore+=2
            if(ans2=='10'):
                totscore+=2
            if(ans3=='4'):
                totscore+=2
            if(ans4=='0'):
                totscore+=2
            if(ans5=='11'):
                totscore+=2
            if(ans6=='9'):
                totscore+=2
            if(ans7=='5'):
                totscore+=2
            if(ans8=='0'):
                totscore+=2
            if(ans9=='0'):
                totscore+=2
            if(ans10=='0'):
                totscore+=2

            totscore=int(totscore)
            obj0.type="calculation"
            obj0.Tscore=totscore
            obj0.save()
            return index5(request)
    return render(request,'test1/act5.html',context={'tform7':tform7})



def index5(request):
        form77=forms.Test5()

        if request.method=='POST':
            form77= forms.Test5(request.POST)
            if form77.is_valid():
                 test66 = Test_r.objects.first()
                  #type_of_test = type(test)
                  #random = str(type_of_test)
                  #length=int(len(test))
                 random1 =test66.Tscore
                 print('object added')
                  #print(type_of_test)
                  #args={'test':test}
                 # test.all()

        return render(request,'test1/index5.html',context={'random1':random1})





def act4(request):
    tform3= forms.Test4()
    print("hello")
    if request.method=='POST':
        tform3=Test4(request.POST)
        if tform3.is_valid():
            obj3=Test_r
            #tform.save(commit=False);
            totscore=0
            ans1=tform3['ans1'].value()
            ans2=tform3['ans2'].value()
            ans3=tform3['ans3'].value()
            ans4=tform3['ans4'].value()
            ans5=tform3['ans5'].value()
            ans6=tform3['ans6'].value()
            ans7=tform3['ans7'].value()
            ans8=tform3['ans8'].value()
            ans9=tform3['ans9'].value()
            ans10=tform3['ans10'].value()


            obj3=tform3.save(commit=False);

            if(ans1=='b'):
                totscore+=2
            if(ans2=='a'):
                totscore+=2
            if(ans3=='a'):
                totscore+=2
            if(ans4=='b'):
                totscore+=2
            if(ans5=='b'):
                totscore+=2
            if(ans6=='a'):
                totscore+=2
            if(ans7=='b'):
                totscore+=2
            if(ans8=='a'):
                totscore+=2
            if(ans9=='b'):
                totscore+=2
            if(ans10=='a'):
                totscore+=2

            totscore=int(totscore)
            obj3.type="basic calc"
            obj3.Tscore=totscore
            obj3.save()
            return index4(request)
    return render(request,'test1/act4.html',context={'tform3':tform3})


def index4(request):
        form6=forms.Test4()

        if request.method=='POST':
            form6= forms.Test4(request.POST)
            if form6.is_valid():
                 test6 = Test_r.objects.first()
                  #type_of_test = type(test)
                  #random = str(type_of_test)
                  #length=int(len(test))
                 random1 =test6.Tscore
                 print('object added')
                  #print(type_of_test)
                  #args={'test':test}
                 # test.all()

        return render(request,'test1/index4.html',context={'random1':random1})



def act3(request):
    tform1= forms.Test3()
    print("hello")
    if request.method=='POST':
        tform1=Test3(request.POST)
        if tform1.is_valid():
            obj11=Test_r
            #tform.save(commit=False);
            totscore=0
            ans1=tform1['ans1'].value()
            ans2=tform1['ans2'].value()
            ans3=tform1['ans3'].value()
            ans4=tform1['ans4'].value()
            ans5=tform1['ans5'].value()
            ans6=tform1['ans6'].value()
            ans7=tform1['ans7'].value()
            ans8=tform1['ans8'].value()
            ans9=tform1['ans9'].value()
            ans10=tform1['ans10'].value()


            obj11=tform1.save(commit=False);

            if(ans1=='l'):
                totscore+=2
            if(ans2=='r'):
                totscore+=2
            if(ans3=='l'):
                totscore+=2
            if(ans4=='r'):
                totscore+=2
            if(ans5=='r'):
                totscore+=2
            if(ans6=='l'):
                totscore+=2
            if(ans7=='l'):
                totscore+=2
            if(ans8=='r'):
                totscore+=2
            if(ans9=='r'):
                totscore+=2
            if(ans10=='l'):
                totscore+=2

            totscore=int(totscore)
            obj11.type="identification"
            obj11.Tscore=totscore
            obj11.save()
            return index3(request)
    return render(request,'test1/act3.html',context={'tform1':tform1})




def index3(request):
    form=forms.Test3()

    if request.method=='POST':
        form2= forms.Test3(request.POST)
        if form2.is_valid():
          test2 = Test_r.objects.first()
          #type_of_test = type(test)
          #random = str(type_of_test)
          #length=int(len(test))
          random1 =test2.Tscore
          print('object added')
          #print(type_of_test)
          #args={'test':test}
         # test.all()

    return render(request,'test1/index3.html',context={'random1':random1})



def index2(request):
    form=forms.Test2()

    if request.method=='POST':
        form= forms.Test2(request.POST)
        if form.is_valid():
          test = Test_r.objects.first()
          #type_of_test = type(test)
          #random = str(type_of_test)
          #length=int(len(test))
          random =test.Tscore
          print('object added')
          #print(type_of_test)
          #args={'test':test}
         # test.all()

    return render(request,'test1/index2.html',context={'random':random})



def reg(request):
    form2=forms.Login()
    form3=forms.Regist()

    if request.method=='POST':
        form2= forms.Login(request.POST)
        if form2.is_valid():
               test = Regist.objects.all()
               length=int(len(test))
               email1=form2['email'].value()
               passwd=form2['password1'].value()
               email1=str(email1)
               passwd=str(passwd)
               # email =test[].paremail
               # password=test[i].password1
               #print(length)
               flag=0
               for x in range(length):
                   email =test[x].paremail
                   password=test[x].password1
                   email=str(email)
                   password=str(password)
                   if((email1==email) and (passwd==password)):
                       flag=1
                       return act1(request)
                   else:
                       flag=0
                   x+=1
               if(flag==1):
                   return act1(request)
               else:
                   return redirect("/regist/")




    return render(request,'test1/reg.html',context={'form2':form2})

# Create your views here.
def registration(request):
    form1=forms.Regist()
    if request.method=='POST':
        form1=forms.Regist(request.POST)
        if form1.is_valid():
            form1.save()
            #obj1.save()
            return redirect("/log/")
    return render(request,'test1/registration.html',context={'form1':form1})



  # form1 = forms.Regist()
  # if request.method=='POST':
  #   form1=Regist(request.POST)
  #   if form1.is_valid():
  #       form1.save()
  #       return redirect("/log/")
  # return render(request,'test1/registration.html',context={'form1':form1})


def index(request):
    form=forms.TestForm1()

    if request.method=='POST':
        form= forms.TestForm1(request.POST)
        if form.is_valid():
          test = OTest.objects.all()
          type_of_test = type(test)
          #random = str(type_of_test)
          length=int(len(test))
          random =test[length-1].Tscore
          random=int(random)
          type_of_random = str(type(random))
          print('object added')
          #print(type_of_test)
          #args={'test':test}
         # test.all()

    return render(request,'test1/index.html',context={'type_of_random':type_of_random,'random':random})

def testform(request):
    form = forms.TestForm1()
    if request.method=='POST':
        form=TestForm1(request.POST)
        if form.is_valid():
            obj=OTest()
            i=1
            totscore=0
            for x in range(15):
                varname = 'ans'+str(i)
                score=form.cleaned_data[varname]
                score=int(score)
                totscore+=score
                i+=1
            obj=form.save(commit=False);
            #if totscore > 15:
                 #obj.Result="Yes"
            #elif:
                 #obj.Result="No"

            obj.Tscore=totscore
            #print(totscore)
            obj.save()
            return index(request)
            print("VALIDATION SUCCESS")
        else:
            print('error')
    return render(request,'test1/testform.html',context={'form':form})
