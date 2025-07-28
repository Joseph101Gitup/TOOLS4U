import random
import string
from django.shortcuts import render,redirect

from AdminApp.models import tbl_location,tbl_district
from GuestApp.models import tbl_login, tbl_seller, tbl_user

from django.http import HttpResponse, JsonResponse

from SellerApp.models import tbl_tool

from email.message import EmailMessage
import smtplib


def Login(request):
    return render(request,'Guest/Login.html')


def login_process (request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if tbl_login.objects.filter(username=username, password=password).exists():
            logindata = tbl_login.objects.get(username=username, password=password)
            request.session['loginId'] = logindata.loginid
            role = logindata.role
            if role == "admin":
                return redirect('/Admin/Adminhome')
            elif role == "seller":
                if logindata.status == 'Accepted':
                    return redirect('/Seller/Sellerhome')
                else:
                    return HttpResponse("<script>alert('Request not accepted');window.location='/Guest/login.html';</script>")
            elif role == "user":
                return redirect('/User/Userhome')
        
        else:
            context = {"error": "Incorrect username or password"}
            return render (request, "Guest/login.html", context)

def Guesthome(request):
    tools=tbl_tool.objects.all()#select * from tbl_tool
    return render(request,'Guest/Index.html',{'tools': tools})

def userRegistration(request):
    districts=tbl_district.objects.all()#select * from tbl_district
    return render(request,'Guest/userRegistration.html',{ 'districts': districts})

def filllocation1(request):
    did = int(request.POST.get("did"))
    location=tbl_location.objects.filter(district_id=did).values()#select * from tbl_location
    return JsonResponse(list(location),safe=False)

def userRegistration_process (request):
    if request.method == 'POST':
        lob = tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "user"
        lob.status = "confirmed"
        if tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Alredy Exists..');window.location='/';</script>")
        else:
            lob.save()
        name = request.POST.get("name")     #textboxname = music
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        location = request.POST.get("location")
        pincod = request.POST.get("pin")
        regdate = request.POST.get("regdate")
        landmark = request.POST.get("landmark")
        
        uob = tbl_user()
        uob.user_name = name  #cob.user_name(fieldname in table) = value (eg:cob.user_name=muscic)
        uob.user_phone = phone
        uob.user_email = email
        uob.user_location = tbl_location.objects.get(location_id=location)
        uob.user_pincode = pincod
        uob.user_landmark = landmark
        uob.user_regdate = regdate
        uob.user_loginid = lob
        if tbl_user.objects.filter(user_name=name).exists():
            return HttpResponse("<script>alert('Alredy Exists..');window.location='/';</script>")
        else:
            uob.save() # insert query
            msg = EmailMessage()
            msg.set_content(f'Dear {name},\n\n'
                
                'Welcome to TOOLS4U! 🎊 We’re thrilled to have you as part of our shopping community.\n\n'
                'If you have any questions, our support team is here to help. Contact us at tools4uservice@gmail.com or 8254693214.\n\n'
                'Happy shopping! 🛍️\n\n'
                
                
                'Best Regards,\n'
                'TOOLS4U\n'
                '[Your Website URL]\n'
                '2589631478'
                    )
  
            msg['Subject'] = "🎉 Welcome to TOOLS4U - Let's Get Started!"
            msg['from'] = 'tools4uservice@gmail.com'
            msg['To'] = email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('tools4uservice@gmail.com','tczr hdlm wnvt luer')
                smtp.send_message(msg)

            return HttpResponse("<script>alert('Sucessfuly inserted');window.location='/';</script>")

def sellerRegistration(request):
    districts=tbl_district.objects.all()#select * from tbl_district
    return render(request,'Guest/sellerRegistration.html',{ 'districts': districts})

def sellerRegistration_process (request):
    if request.method == 'POST':
        lob = tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "seller"
        lob.status = "Requested"
        if tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Alredy Exists..');window.location='/';</script>")
        else:
            lob.save()
        name = request.POST.get("name")     #textboxname = music
        phone = request.POST.get("phone")
        image = request.FILES["image"]
        email = request.POST.get("email")
        location = request.POST.get("location")
        pincod = request.POST.get("pin")
        idproof = request.FILES["idproof"]
        regdate = request.POST.get("regdate")
        landmark = request.POST.get("landmark")
        
        sob = tbl_seller()
        sob.seller_name = name  #cob.user_name(fieldname in table) = value (eg:cob.user_name=muscic)
        sob.seller_phone = phone
        sob.seller_image = image
        sob.seller_email = email
        sob.seller_location = tbl_location.objects.get(location_id=location)
        sob.seller_pincode = pincod
        sob.seller_landmark = landmark
        sob.seller_idproof = idproof
        sob.seller_regdate = regdate
        sob.seller_loginid = lob
        if tbl_seller.objects.filter(seller_name =name).exists():
            return HttpResponse("<script>alert('Alredy Exists..');window.location='/';</script>")
        else:
            sob.save() # insert query
            msg = EmailMessage()
            msg.set_content(f'Dear {name},\n\n'
                
                'Welcome to TOOLS4U! 🎊 We’re thrilled to have you as part of our shopping community.\n\n'
                'If you have any questions, our support team is here to help. Contact us at tools4uservice@gmail.com or 8254693214.\n\n'
                'Happy shopping! 🛍️\n\n'
                
                
                'Best Regards,\n'
                'TOOLS4U\n'
                '[Your Website URL]\n'
                '2589631478'
            )
            
            msg['Subject'] = "🎉 Welcome to TOOLS4U - Let's Get Started!"
            msg['from'] = 'tools4uservice@gmail.com'
            msg['To'] = email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('tools4uservice@gmail.com','tczr hdlm wnvt luer')
            smtp.send_message(msg)
            return HttpResponse("<script>alert('Sucessfuly inserted');window.location='/';</script>")

def Forgot_password(request):
    return render(request,'Guest/Forgot_password.html')

def forgotpassword(request):
    if request.method == 'POST':
        uname = request.POST.get("name")
        # Check if the user is a customer
        if tbl_user.objects.filter(user_loginid__username=uname).exists():
            cust = tbl_user.objects.get(user_loginid__username=uname)
            email = cust.user_email
            customer_name = cust.user_name
            user_type = 'user'
        elif tbl_seller.objects.filter(seller_loginid__username=uname).exists():
            emp = tbl_seller.objects.get(seller_loginid__username=uname)
            email = emp.seller_email
            employee_name = emp.seller_name
            user_type = 'seller'
        else:
            return HttpResponse(
                "<script>alert('No user found with this username.');window.location='/Forgot_password';</script>")
        characters = string.ascii_letters + string.digits
        random_number = ''.join(random.choice(characters) for _ in range(8))
        # Update password for the user
        login_instance = tbl_login.objects.get(username=uname)
        login_instance.password = random_number
        login_instance.save()
        # Email configuration
        msg = EmailMessage()
        if user_type == 'user':
            msg.set_content(f'Hi {customer_name}, Your new password to login in is {random_number}')
        elif user_type == 'turf':
            msg.set_content(f'Hi {employee_name}, Your new password to login in is {random_number}')
        msg['Subject'] = "Forgot Password"
        msg['From'] = 'tools4uservice@gmail.com'
        msg['To'] = email
        # SMTP connection and sending email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('tools4uservice@gmail.com','tczr hdlm wnvt luer')
            smtp.send_message(msg)
        return HttpResponse(
            "<script>alert('Login with the new password sent to your email.');window.location='/Login';</script>")
    return render(request, "Guest/Forgot_password.html")

def contact(request):
    return render(request,'Guest/contact.html')

def IndexG(request):
    return render(request,'Guest/Index.html')



# Create your views here.
