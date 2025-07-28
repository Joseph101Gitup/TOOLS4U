from datetime import date
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control

from AdminApp.models import tbl_category
from GuestApp.models import tbl_user
from SellerApp.models import tbl_tool
from UserApp.models import tbl_purchasepayment, tbl_purchaserequest, tbl_rentpayment, tbl_rentrequest


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    loginid = request.session.get("loginId")
    if loginid:
        return render(request,'User/index.html')
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Userhome(request):
    loginid = request.session.get("loginId")
    if loginid:
        user=tbl_user.objects.get(user_loginid__loginid=loginid)
        tools=tbl_tool.objects.all()#select * from tbl_tool
        category=tbl_category.objects.all()#select * from tbl_category
        return render(request,'User/Index.html',{ 'user': user,'category': category,'tools':tools})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def filltools(request):
    loginid = request.session.get("loginId")
    if loginid:
        scid = int(request.POST.get("scid"))
        type=request.POST.get('type')
        tools=tbl_tool.objects.select_related('subcategory_id').filter(tool_subcategory=scid,tool_type=type).values()#select * from tbl_tool
        return JsonResponse(list(tools),safe=False)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def producturl(request,id,type1):
    loginid = request.session.get("loginId")
    if loginid:
        tools=tbl_tool.objects.filter(tool_id=id).values()#select * from tbl_tool
        return render(request,'User/producturl.html',{ 'tools': tools,'type':type1})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def productRent(request):
    loginid = request.session.get("loginId")
    if loginid:
        id = int(request.POST.get("toolid"))
        qty=request.POST.get('qty')
        tprice=request.POST.get('totalamount')
        user= tbl_user.objects.get(user_loginid__loginid=request.session.get('loginId')  )
  
        if request.POST.get('send') == "Request to Rent":
            fromDate=request.POST.get('rentDate')
            toDate=request.POST.get('rentToDate')
        # return HttpResponse(seller)
            rob=tbl_rentrequest()
            rob.request_toolid = tbl_tool.objects.get(tool_id = id)
            rob.request_quantity = qty
            rob.request_tprice = tprice
            rob.request_userid = user
            rob.request_date = date.today()
            rob.request_requireddate  =  fromDate
            rob.request_returndate = toDate 
            rob.request_Remark = "NULL"
            rob.request_Status = "Requested"
            rob.save() # insert query
            return HttpResponse("<script>alert('Request Sucessfuly');window.location='/User/Userhome/';</script>")
        else:       
            timp=request.POST.get('toolimg')
            tname=request.POST.get('name')
            tamount=request.POST.get('totalamount')
            id = int(request.POST.get("toolid"))
            qty=request.POST.get('qty')
            stock = request.POST.get('stock')
            return render(request,'User/payment.html',{'name': tname,'timp': timp,'tamount':tamount,'tid':id,'qty':qty,'stock':stock})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")
 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def payment_process (request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == 'POST':
            tid = request.POST.get("tid")
            tamount = request.POST.get("totalamount")
            qty = int(request.POST.get("qty"))
            tob = tbl_tool.objects.get(tool_id=tid)
            newstock = tob.tool_stock - qty
            tob.tool_stock = newstock
            tob.save()
            pob = tbl_purchaserequest()
            pob.purchase_toolid = tbl_tool.objects.get(tool_id = tid)
            pob.purchase_quantity = request.POST.get("qty")
            pob.purchase_tprice = request.POST.get("totalamount")
            pob.purchase_userid = tbl_user.objects.get(user_loginid__loginid=request.session.get('loginId')  )
            pob.purchase_date = date.today()
            pob.purchase_stock = newstock
            pob.purchase_Status = "Paid"
            pob.save()        
            ppyob = tbl_purchasepayment()
            ppyob.ppayment_amount = tamount
            ppyob.ppayment_userid = tbl_user.objects.get(user_loginid__loginid=request.session.get('loginId')  )
            ppyob.ppayment_purchaserequestid = pob
            ppyob.ppayment_date = date.today()
            ppyob.ppayment_status = "Paid"
            ppyob.save() # insert query
            return HttpResponse("<script>alert('Payment Sucessfuly');window.location='/User/Userhome/';</script>")
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def rentedProductsView(request):
    loginid = request.session.get("loginId")
    if loginid:
        rproducts=tbl_rentrequest.objects.all().values()#select * from tbl_tool
        return render(request,'User/rentedProductsView.html',{ 'rproducts': rproducts})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillRequestedOption(request):
    loginid = request.session.get("loginId")
    if loginid:
        rqo = request.POST.get("rqo")
        loginid=request.session['loginId']
        requested=tbl_rentrequest.objects.filter(request_Status=rqo,request_userid__user_loginid__loginid=loginid).values('request_toolid_id','request_toolid__tool_photo','request_quantity','request_tprice','request_toolid__tool_name','request_toolid__tool_price')
        return JsonResponse(list(requested),safe=False)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillAcceptedOption(request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == "POST":
            rqo = request.POST.get("rqo")
            loginid = request.session.get('loginId')

            if not loginid:
                return JsonResponse({'error': 'User not logged in'}, status=403)

            # Get all paid request IDs from tbl_rentpayment
            paid_request_ids = tbl_rentpayment.objects.filter(
                rpayment_status="Paid"
            ).values_list("rpayment_rentrequestid_id", flat=True)

            requested = tbl_rentrequest.objects.filter(
                request_Status=rqo, 
                request_userid__user_loginid__loginid=loginid  #   Exclude paid requests
            ).exclude(request_id__in=paid_request_ids).values(
                'request_id',
                'request_toolid_id',  # Added ID to use for edit link
                'request_toolid__tool_photo',
                'request_quantity',
                'request_tprice',
                'request_toolid__tool_name',
                'request_toolid__tool_price'
            )

            return JsonResponse(list(requested), safe=False)
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillRejectedOption(request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == "POST":
            rqo = request.POST.get("rqo")
            loginid = request.session.get('loginId')

            if not loginid:
                return JsonResponse({'error': 'User not logged in'}, status=403)

            requested = tbl_rentrequest.objects.filter(
                request_Status=rqo, 
                request_userid__user_loginid__loginid=loginid
            ).values(
                'request_toolid_id',  # Added ID to use for edit link
                'request_toolid__tool_photo',
                'request_quantity',
                'request_tprice',
                'request_Remark',
                'request_toolid__tool_name',
                'request_toolid__tool_price'
            )

            return JsonResponse(list(requested), safe=False)
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillPaidOption(request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == "POST":
            rqo = request.POST.get("rqo")
            loginid = request.session.get('loginId')

            if not loginid:
                return JsonResponse({'error': 'User not logged in'}, status=403)

            requested = tbl_rentpayment.objects.filter(
                rpayment_status=rqo, 
                rpayment_userid__user_loginid__loginid=loginid
            ).select_related('rpayment_rentrequestid').values(
                'rpayment_rentrequestid__request_toolid_id',  # Added ID to use for edit link
                'rpayment_rentrequestid__request_toolid__tool_photo',
                'rpayment_rentrequestid__request_quantity',
                'rpayment_rentrequestid__request_tprice',
                'rpayment_date',
                'rpayment_userid__user_name',
                'rpayment_rentrequestid__request_toolid__tool_name',
                'rpayment_rentrequestid__request_toolid__tool_price'
            )

            return JsonResponse(list(requested), safe=False)
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def rentPayment(request,id):
    loginid = request.session.get("loginId")
    if loginid:
        rproducts = tbl_rentrequest.objects.select_related('request_toolid').get(request_id=id)
        return render(request,'User/rentPayment.html',{ 'rproducts': rproducts})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def rentPayment_process (request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == 'POST':
            tid = request.POST.get("tid")
            tamount = request.POST.get("totalamount")
            qty = int(request.POST.get("qty"))
            tob = tbl_tool.objects.get(tool_id=tid)
            newstock = tob.tool_stock - qty
            tob.tool_stock = newstock
            tob.save()    
            rid = request.POST.get("rid")
            rob = tbl_rentrequest.objects.get(request_id = rid)
            rpyob = tbl_rentpayment()
            rpyob.rpayment_amount = tamount
            rpyob.rpayment_userid = tbl_user.objects.get(user_loginid__loginid=request.session.get('loginId')  )
            rpyob.rpayment_rentrequestid = rob
            rpyob.rpayment_date = date.today()
            rpyob.rpayment_status = "Paid"
            rpyob.save() # insert query
            return HttpResponse("<script>alert('Payment Sucessfuly');window.location='/User/Userhome/';</script>")
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def purchasedProductView(request):
    loginid = request.session.get("loginId")
    if loginid:
        pproducts = tbl_purchasepayment.objects.select_related('ppayment_purchaserequestid').values(
            'ppayment_date',
            'ppayment_id',
            'ppayment_purchaserequestid__purchase_toolid__tool_photo',
            'ppayment_purchaserequestid__purchase_toolid__tool_name',
            'ppayment_purchaserequestid__purchase_quantity',
            'ppayment_amount',
            'ppayment_purchaserequestid__purchase_userid__user_name')
        # return HttpResponse(pproducts)
        return render(request,'User/purchasedProductView.html',{ 'pproducts': pproducts})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")
   
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    loginid = request.session.get("loginId")
    if loginid:
        request.session.clear()  #clears session variable only
        return redirect('/')
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def packageTracking(request,id):
    loginid = request.session.get("loginId")
    if loginid:
        pproducts=tbl_purchasepayment.objects.filter(
                ppayment_userid__user_loginid__loginid=loginid,
                ppayment_id = id
            ).select_related('ppayment_purchaserequestid').values(
                'ppayment_status',  # Added ID to use for edit link
                'ppayment_purchaserequestid__purchase_toolid__tool_name'
            )
        return render(request,'User/packageTracking.html',{ 'pproducts': pproducts})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

def contactU(request):
    loginid = request.session.get("loginId")
    if loginid:
        return render(request,'User/contactU.html')
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

# Create your views here.
