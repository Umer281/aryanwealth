from django.db import models
import datetime

class RegisteredAds(models.Model):
    email= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    class Meta:
        db_table = "ads"

    @staticmethod
    def get_customer_by_email(email):
        try:
            return RegisteredAds.objects.get(email=email)
        except:
            return False


"""class RegisteredForms(models.Model):
    username= models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    phone_number= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    edate = models.DateField(auto_now=True)"""

class RegisteredForms(models.Model):
    username= models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    phone_number= models.CharField(max_length=200)
    verify= models.BooleanField(default=0)
    password= models.CharField(max_length=200)
    edate = models.DateField(auto_now=True)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return RegisteredForms.objects.get(email=email)
        except:
            return False



class stock(models.Model):
    Call=models.CharField(max_length=30,default="")
    Timee=models.CharField(max_length=20,default="")
    Script=models.CharField(max_length=30,default="")
    Price=models.CharField(max_length=30,default="")
    TGT1_PTS=models.CharField(max_length=30,default="")
    TGT2_PTS=models.CharField(max_length=30,default="")
    TGT3_PTS=models.CharField(max_length=30,default="")
    LTP = models.CharField(max_length=30,default="")
    SL = models.CharField(max_length=10,default="")
    Remarks=models.CharField(max_length=100,default="")
    Date = models.DateField(default=datetime.date.today)
    ShowToUsers=models.BooleanField(default=False)
    TGT1 = models.BooleanField(default=True)
    TGT2 = models.BooleanField(default=True)
    TGT3 = models.BooleanField(default=True)
    SL_Flag = models.BooleanField(default=True)

class Employee(models.Model):
    edate = models.DateField(auto_now=True)
    estock = models.CharField(max_length=20)
    eentryprise = models.CharField(max_length=100)
    equantity = models.CharField(max_length=100)
    eplntgt1 = models.IntegerField()
    eplntgt2 = models.IntegerField()
    eplntgt3 = models.IntegerField()

    class Meta:
        db_table = "employee"
