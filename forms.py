from django import forms
from test1.models import OTest
from django.core import validators
from test1.models import Regist
from test1.models import Test_r


ans= [
    ('2', 'YES'),
    ('1', 'Frequently'),
    ('idk', 'NO'),
    ]


ans2= [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
    ]

yn= [
    ('y', 'yes'),
    ('n', 'no'),
    ('idk', 'i dont know ')
    ]


lr= [
    ('l', 'left'),
    ('r', 'right'),
    ('idk', 'i dont know ')
    ]

ba= [
    ('b', 'Before'),
    ('a', 'after'),
    ('idk', 'i dont knw'),
    ]


class Test5(forms.ModelForm):
    class Meta():
        model=Test_r
        fields='__all__'
    name= forms.CharField(label="enter name")
    type= forms.CharField(widget = forms.HiddenInput(),required=False)
    ans1= forms.CharField(label="3 + 2=")
    ans2= forms.CharField(label="5 + 5=")
    ans3= forms.CharField(label="10 - 6=")
    ans4= forms.CharField(label="8 - 8=")
    ans5= forms.CharField(label="11 + 0=")
    ans6= forms.CharField(label="5 + 4=  ")
    ans7= forms.CharField(label="8 - 3=")
    ans8= forms.CharField(label="0 + 0=")
    ans9= forms.CharField(label="0 - 0=")
    ans10= forms.CharField(label="3 - 3=")
    Tscore=forms.CharField(widget = forms.HiddenInput(),required=False)


class Test2(forms.ModelForm):
    class Meta():
        model=Test_r
        fields='__all__'
    name= forms.CharField(label="enter name")
    type= forms.CharField(widget = forms.HiddenInput(),required=False)
    ans1= forms.CharField(label="10 > 5",widget=forms.RadioSelect(choices=yn))
    ans2= forms.CharField(label="2 > 5",widget=forms.RadioSelect(choices=yn))
    ans3= forms.CharField(label="6 > 5",widget=forms.RadioSelect(choices=yn))
    ans4= forms.CharField(label="7 > 7",widget=forms.RadioSelect(choices=yn))
    ans5= forms.CharField(label="10 > 11",widget=forms.RadioSelect(choices=yn))
    ans6= forms.CharField(label="5 > 15",widget=forms.RadioSelect(choices=yn))
    ans7= forms.CharField(label="23 > 51",widget=forms.RadioSelect(choices=yn))
    ans8= forms.CharField(label="30 > 50",widget=forms.RadioSelect(choices=yn))
    ans9= forms.CharField(label="300 > 335",widget=forms.RadioSelect(choices=yn))
    ans10= forms.CharField(label="5 > 0",widget=forms.RadioSelect(choices=yn))
    Tscore=forms.CharField(widget = forms.HiddenInput(),required=False)


class Test3(forms.ModelForm):
    class Meta():
        model=Test_r
        fields='__all__'
    name= forms.CharField(label="enter name")
    type= forms.CharField(widget = forms.HiddenInput(),required=False)
    ans1= forms.CharField(label="Which one is SIX? 6 or 9",widget=forms.RadioSelect(choices=lr))
    ans2= forms.CharField(label="Which one is SEVEN? 1 or 7",widget=forms.RadioSelect(choices=lr))
    ans3= forms.CharField(label="Which one is EIGHT? 8 or 0",widget=forms.RadioSelect(choices=lr))
    ans4= forms.CharField(label="Which one is FIVE? 6 or 5",widget=forms.RadioSelect(choices=lr))
    ans5= forms.CharField(label="Which one is THREE? 8 or 3",widget=forms.RadioSelect(choices=lr))
    ans6= forms.CharField(label="Which one is ONE? 9 or 1",widget=forms.RadioSelect(choices=lr))
    ans7= forms.CharField(label="Which one is NINE? 9 or 6",widget=forms.RadioSelect(choices=lr))
    ans8= forms.CharField(label="Which one is TWO? 7 or 2",widget=forms.RadioSelect(choices=lr))
    ans9= forms.CharField(label="Which one is FOUR? 5 OR 4",widget=forms.RadioSelect(choices=lr))
    ans10= forms.CharField(label="Which one is TEN? 10 or 01",widget=forms.RadioSelect(choices=lr))
    Tscore=forms.CharField(widget = forms.HiddenInput(),required=False)

class Test4(forms.ModelForm):
    class Meta():
        model=Test_r
        fields='__all__'
    name= forms.CharField(label="enter name")
    type= forms.CharField(widget = forms.HiddenInput(),required=False)
    ans1= forms.CharField(label="10 ___ 12",widget=forms.RadioSelect(choices=ba))
    ans2= forms.CharField(label="1 ___ 0",widget=forms.RadioSelect(choices=ba))
    ans3= forms.CharField(label="110 ___ 101",widget=forms.RadioSelect(choices=ba))
    ans4= forms.CharField(label="102 ___ 120",widget=forms.RadioSelect(choices=ba))
    ans5= forms.CharField(label="40 ___ 44",widget=forms.RadioSelect(choices=ba))
    ans6= forms.CharField(label="58 ___ 50",widget=forms.RadioSelect(choices=ba))
    ans7= forms.CharField(label="3 ___ 6",widget=forms.RadioSelect(choices=ba))
    ans8= forms.CharField(label="80 ___ 76",widget=forms.RadioSelect(choices=ba))
    ans9= forms.CharField(label="34 ___ 43",widget=forms.RadioSelect(choices=ba))
    ans10= forms.CharField(label="99 ___ 96",widget=forms.RadioSelect(choices=ba))
    Tscore=forms.CharField(widget = forms.HiddenInput(),required=False)



class Regist(forms.ModelForm):

     class Meta():
         model=Regist
         fields='__all__'
     name= forms.CharField(label="Enter name of child")
     phone=forms.CharField(label="Parent's phone number",validators=[validators.MinLengthValidator(10),validators.MaxLengthValidator(10),])
     age= forms.IntegerField(label="enter age of child", validators=[validators.MaxValueValidator(10),validators.MinValueValidator(3)])
     password1 = forms.CharField(widget=forms.PasswordInput(),validators=[validators.MinLengthValidator(8)])
     paremail= forms.EmailField(label="Parent's email id")
     gender=forms.CharField(label="select gender",widget=forms.RadioSelect(choices=ans2))


class TestForm1(forms.ModelForm):

    class Meta():
        model=OTest
        fields='__all__'
    ans1= forms.CharField(label="Did your child struggle to learn to count?",widget=forms.RadioSelect(choices=ans))
    ans2= forms.CharField(label="Does she say numbers out of order — long after peers have mastered this skill?",widget=forms.RadioSelect(choices=ans))
    ans3= forms.CharField(label="Does your child have difficulty writing numbers clearly or keeping his work neat when solving math problems?",widget=forms.RadioSelect(choices=ans))
    ans4= forms.CharField(label="Does your child not seem to understand the connection between the symbol “4” and the word “four?” Does he make mistakes when reading or following directions involving number words and symbols?",widget=forms.RadioSelect(choices=ans))
    ans5= forms.CharField(label="Does your child struggle to connect the concept of numbers to real-world items? When you ask him how many cookies are left, for example, does he seem confused by the question or answer incorrectly?",widget=forms.RadioSelect(choices=ans))
    ans6= forms.CharField(label="Does your child not seem to understand the difference between adding and subtracting? Does she confuse the + and – symbols when completing math problems? ",widget=forms.RadioSelect(choices=ans))
    ans7= forms.CharField(label="Does your child still count on his fingers past third grade?",widget=forms.RadioSelect(choices=ans))
    ans8= forms.CharField(label="Does your child have difficulty telling time on an analog clock?",widget=forms.RadioSelect(choices=ans))
    ans9= forms.CharField(label="Does your child struggle to understand money, and have difficulty making change or sticking to a budget?",widget=forms.RadioSelect(choices=ans))
    ans10= forms.CharField(label="Does your child get lost, even in familiar surroundings?",widget=forms.RadioSelect(choices=ans))
    ans11= forms.CharField(label="Does your child struggle to read graphs or charts without help",widget=forms.RadioSelect(choices=ans))
    ans12= forms.CharField(label="Does your child struggle to sort objects by shape, color, or size?",widget=forms.RadioSelect(choices=ans))
    ans13= forms.CharField(label="Does your child have difficulty applying fractions to real-world objects? Is she unable to determine that a dollar equals four quarters, for instance, or that one-half of the year is equal to six months?",widget=forms.RadioSelect(choices=ans))
    ans14= forms.CharField(label="Does your child ever get unnaturally upset or complain of feeling ill while completing math homework?",widget=forms.RadioSelect(choices=ans))
    ans15= forms.CharField(label="Does your child have trouble solving word problems or multi-step math problems? Does she struggle to articulate what strategies she’ll use along the way?",widget=forms.RadioSelect(choices=ans))
    Tscore=forms.CharField(widget = forms.HiddenInput(),required=False)
    #Result=forms.CharField(widget = forms.HiddenInput(),required=False)



class Login(forms.Form):
    email=forms.EmailField()
    password1=forms.CharField(widget=forms.PasswordInput())
