from django.contrib import messages
from .forms import FormRegisterForm
from .models import stock, RegisteredAds, Employee
import datetime
from .models import RegisteredForms
#from .models import RegisteredAdmin
from django.shortcuts import render , HttpResponseRedirect, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required



## Updated upstream
#---------------------------home pages add from here--------------------
from .scrap import find_shares

## Stashed changes

print(make_password('123'))



#home pages add from herepython manage.py runserver
def indexV(request):    
    return render(request, 'index.html', )

#def loginV(request):    return render(request, 'login.html', )
"""def loginV(request):
    if request.method == "POST":
        try:
            Userdetails=RegisteredForms.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            return render(request,'welcome.html')
        except RegisteredForms.DoesNotExist as e:
            messages.success(request,'Invalid user or login .....')
    return render(request,'login.html')"""

def loginV(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        verify = RegisteredForms.objects.filter(verify=1)
        customer = RegisteredForms.get_customer_by_email(email)
        error_message = None
        if verify:
            if customer:
                flag = check_password(password, customer.password)
                if flag:
                    request.session['customer'] = customer.id
                    return render(request,'welcome.html')
                else:
                    error_message = 'Email or Password invalid !!'
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Please Wait Admin Approve !!'

        print(email, password)

    return render(request, 'login.html')



def aboutV(request):    return render(request, 'about.html', )

def complaintV(request):    return render(request, 'complaint.html',)

def contactV(request):      return render(request, 'contact.html',)

#def day_wise_summary_profit_and_lossV(request): return render(request, 'day_wise_summary_profit_and_loss.html',)

def day_wise_summary_profit_and_lossV(request):
    employees = Employee.objects.all()
    return render(request, 'day_wise_summary_profit_and_loss.html',{'employees':employees})


def disclaimerV(request):   return render(request, 'disclaimer.html',)

def faqV(request):          return render(request, 'faq.html',)

def mycoursesV(request):    return render(request, 'mycourses.html',)

def past_performanceV(request):     return render(request, 'past_performance.html',)

#def pastperformanceV(request):      return render(request, 'pastperformance.html', )

def refundV(request):               return render(request, 'refund.html', )

# def registerV(request):
#     form = FormRegisterForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context = {'FormRegisterForm': FormRegisterForm }
#     return render(request, 'register.html',context)




def registerV(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        password=request.POST['password']
        password1=make_password(password)
        RegisteredForms(username=username,email=email,phone_number=phone_number,password=password1).save()
        messages.success(request,'The new user ' +request.POST['username']+ "is saved successfully" )
        return render(request,'register.html')
    else:
        return render(request,'register.html')


# Updated upstream
#---------------------------------- user registration page from here---------------------------------------
#> Stashed changes



# Updated upstream
def servicesV(request):             return render(request, 'services.html',)

def stock_wise_details_profit_and_lossV(request):       return render(request, 'stock_wise_details_profit_and_loss.html',)

def terms_and_conditionsV(request):                     return render(request, 'terms_and_conditions.html',)
#----------------------------- pages in admin pannel -----------------------------------------
#@login_required(login_url="login_page")
def admin_dashboardV(request):
    return render(request, 'admin/dashboard.html', )


#def admin_total_usersV(request):    return render(request, 'admin/total_user.html', )

#def admin_change_passwordV(request):    return render(request, 'admin/change_password.html', )

#----------------------------   show user in admin pannel  -------------------------------
#@login_required(login_url="login_page")
def admin_total_userV(request):
    employees = RegisteredForms.objects.all()
    return render(request, 'admin/total_user.html', {'employees': employees})

#----------------------------- delete user from admin section  --------------------------
"""
def destroy(request, id):
    employees = RegisteredForms.objects.get(id=id)
    employees.delete()
    return redirect("/admin")"""
"""def delete(request,i_id):
    stock.objects.filter(id=i_id).delete()
    return HttpResponseRedirect("/admin_table")"""

#-------------------------------------  admin login and authentication ---------------------

"""def admin_loginV(request):
    if request.method == "POST":
        try:
            Userdetails=RegisteredForms.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            return render(request,'admin/dashboard.html')
        except RegisteredForms.DoesNotExist as e:
            messages.success(request,'Invalid user or login .....')
    return render(request,'admin/login.html')"""

def admin_loginV(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = RegisteredAds.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return render(request,'admin/dashboard.html')
            else:
                    error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
    return render(request,'admin/login.html')




"""def loginV(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = RegisteredForms.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return render(request,'welcome.html')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
    return render(request, 'login.html')"""

#--------------------------------- user page with authentication -------------------------------------
# Stashed changes

def welcomeV(request):                                  return render(request, 'welcome.html',)
def admin_swing(request):                                  return render(request, 'admin/swing.html',)
def users_swing(request):                                  return render(request, 'users/swing.html',)


#---------------------------------------- delete live data  ---------------------------------------

def delete(request, i_id):
    stock.objects.filter(id=i_id).delete()
    return HttpResponseRedirect("/admin_table")
#------------------------------------- add a new data to user pannel -----------------------------------
# Stashed changes

def addtouser(request,i_id):
    value = stock.objects.get(id=i_id)
    value.ShowToUsers = True
    value.save()
    return HttpResponseRedirect("/admin_table")

#------------------------------------------- edit live data table ------------------------------------------

def edit(request, i_id):
    stock1 = stock.objects.get(id=i_id)

    if request.method == "POST":
        sell1 = request.POST['Call']
        sell2 = request.POST['Time']
        sell3 = request.POST['Script']
        sell4 = request.POST['Price']
        sell5 = request.POST['TGT1_PTS']
        sell6 = request.POST['TGT2_PTS']
        sell7 = request.POST['TGT3_PTS']
        sell8 = request.POST['Remarks']
        sell9 = request.POST['SL']

        stock1.Call = sell1
        stock.Time = sell2
        stock1.Script = sell3
        stock1.Price = sell4
        stock1.TGT1_PTS = sell5
        stock1.TGT2_PTS = sell6
        stock1.TGT3_PTS = sell7
        stock1.Remarks = sell8
        stock1.SL = sell9

        stock1.save()

        return HttpResponseRedirect("/admin_table")

    remark = stock1.Remarks
    return render(request, 'admin/edit.html', {'name': stock1, 'remark': remark, })


def admin_home(request):
    return render(request, 'admin/dashboard.html')

def admin_tableV(request):

    if request.method=="POST":
        sell1=request.POST['Call']
        sell2=request.POST['Time']
        sell3=request.POST['Script']
        sell4=request.POST['Price']
        sell5=request.POST['TGT1_PTS']
        sell6=request.POST['TGT2_PTS']
        sell7=request.POST['TGT3_PTS']
        sell8=request.POST['Remarks']
        sell9=request.POST['SL']

        stock1 = stock.objects.create()    # New Row In Database

        stock1.Call=sell1
        stock.Time=sell2
        stock1.Script=sell3
        stock1.Price=sell4
        stock1.TGT1_PTS=sell5
        stock1.TGT2_PTS=sell6
        stock1.TGT3_PTS=sell7
        stock1.Remarks=sell8
        stock1.SL=sell9
        stock1.LTP = find_shares(sell3)
        stock1.save()

        return HttpResponseRedirect("/admin_table")

    values = stock.objects.filter(Date=datetime.date.today())
    return render(request, 'admin/table.html',{'list':values})

def function(value):
    new=""
    for i in value:
        if i=="/":
            break
        else:
            new+=i
    return new


def ajaxdata(request):
    values = stock.objects.filter(ShowToUsers=1, Date=datetime.date.today())
    for i in values:
        company = i.Script
        ltpp = find_shares(company)
        i.LTP = ltpp

        tgt1 = float(function(i.TGT1_PTS))
        tgt2 = float(function(i.TGT2_PTS))
        tgt3 = float(function(i.TGT3_PTS))
        ltp = float(i.LTP)
        sl = float(function(i.SL))
        sl_flag = i.SL_Flag

        if sl >= ltp and sl_flag:
            i.Remarks = ""
            i.Remarks = "Stop Loss"
            i.SL_Flag = False
            sl_flag = False

        elif (i.TGT1 or i.TGT2 or i.TGT2) and sl_flag:

            if ltp >= tgt1 and i.TGT1:
                remarks = i.Remarks
                remarks += "TGT1 Hit,"
                i.Remarks = remarks
                i.TGT1 = False

            if ltp >= tgt2 and i.TGT2:
                remarks = i.Remarks
                remarks += "TGT2 Hit,"
                i.Remarks = remarks
                i.TGT2 = False

            if ltp >= tgt3 and i.TGT3:
                remarks = i.Remarks
                remarks += "TGT3 Hit,"
                i.Remarks = remarks
                i.TGT3 = False

        i.save()

    return render(request, "admin/ajaxdata.html", {'list': values})


def users_tableV(request):
    return render(request, 'users/table.html')


def users_tableV(request):
    return render(request, 'users/table.html')

#admin
#def admin_loginV(request):    return render(request, 'admin/login.html', )
# Updated upstream
"""
def admin_loginV(request):
    if request.method == "POST":
        try:
            Userdetails=RegisteredAdmin.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            return render(request,'welcome.html')
        except RegisteredAdmin.DoesNotExist as e:
            messages.success(request,'Invalid user or login .....')
    return render(request,'table.html')"""

"""def admin_loginV(request):
    if request.method == "POST":
        try:
            Userdetails=RegisteredAds.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            return render(request,'admin/dashboard.html')
        except RegisteredAds.DoesNotExist as e:
            messages.success(request,'Invalid user or login .....')
    return render(request,'admin/login.html')"""



#def admin_dashboardV(request):    return render(request, 'admin/dashboard.html', )

#def admin_total_usersV(request):
    #return render(request, 'admin/total_user.html', )
@login_required(login_url="login_page")
def admin_change_passwordV(request):
    return render(request, 'admin/change_password.html', )


# Stashed changes





