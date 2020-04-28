from django.db import models

class Regist(models.Model):

    name=models.CharField(max_length=128);
    age=models.CharField(max_length=128);
    password1=models.CharField(max_length=100);
    paremail=models.CharField(max_length=128);
    phone=models.CharField(max_length=128);
    gender=models.CharField(max_length=128);

    def __str(self):
      return self.name
      return self.age
      return self.password1
      return self.paremail
      return self.phone
      return self.gender



class Test_r(models.Model):
    name=models.CharField(max_length=128);
    type=models.CharField(max_length=128);
    ans1=models.CharField(max_length=128);
    ans2=models.CharField(max_length=128);
    ans4=models.CharField(max_length=128);
    ans5=models.CharField(max_length=128);
    ans6=models.CharField(max_length=128);
    ans7=models.CharField(max_length=128);
    ans8=models.CharField(max_length=128);
    ans9=models.CharField(max_length=128);
    ans10=models.CharField(max_length=128);
    Tscore=models.CharField(max_length=128,null=True);
    def __str(self):
      return self.name;
      return self.type;
      return self.ans1
      return self.ans2
      return self.ans3
      return self.ans4
      return self.ans5
      return self.ans6
      return self.ans7
      return self.ans8
      return self.ans9
      return self.ans10
      return self.Tscore


class OTest(models.Model):

    ans1=models.CharField(max_length=128);
    ans2=models.CharField(max_length=128);
    ans4=models.CharField(max_length=128);
    ans5=models.CharField(max_length=128);
    ans6=models.CharField(max_length=128);
    ans7=models.CharField(max_length=128);
    ans8=models.CharField(max_length=128);
    ans9=models.CharField(max_length=128);
    ans10=models.CharField(max_length=128);
    ans11=models.CharField(max_length=128);
    ans12=models.CharField(max_length=128);
    ans13=models.CharField(max_length=128);
    ans14=models.CharField(max_length=128);
    ans15=models.CharField(max_length=128);
    Tscore=models.CharField(max_length=128,null=True);
    #Result=models.CharField(max_length=128,null=True);


    def __str(self):
      return self.ans1
      return self.ans2
      return self.ans3
      return self.ans4
      return self.ans5
      return self.ans6
      return self.ans7
      return self.ans8
      return self.ans9
      return self.ans10
      return self.ans11
      return self.ans12
      return self.ans13
      return self.ans14
      return self.ans15
      return self.Tscore
      #return self.Result
