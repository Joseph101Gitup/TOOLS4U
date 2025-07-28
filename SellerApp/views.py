from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_control

from AdminApp.models import tbl_category, tbl_district, tbl_location, tbl_subcategory
from GuestApp.models import tbl_login, tbl_seller
from SellerApp.models import tbl_tool
from UserApp.models import tbl_purchasepayment, tbl_purchaserequest, tbl_rentpayment, tbl_rentrequest

#New import Excel

import xlwt

from django.views.generic import View

#End of new import Excel
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Sellerhome(request):
    loginid = request.session.get("loginId")
    if loginid:
        seller=tbl_seller.objects.get(seller_loginid__loginid=loginid)
        request.session['sellername']=seller.seller_name
        request.session['sellerimage'] = seller.seller_image.url 
        request.session['selleremail']=seller.seller_email
        request.session['sellerid']=seller.seller_id 
        return render(request,'Seller/Index.html')
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def toolsRegistration(request):
    loginid = request.session.get("loginId")
    if loginid:
        category=tbl_category.objects.all()#select * from tbl_category
        return render(request,'Seller/toolsRegistration.html',{ 'category': category})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def toolsRegistration_process (request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == 'POST':
            toolname = request.POST.get("txtname")            #textboxname = music
            toolimage = request.FILES["txtphoto"]
            tooldiscription = request.POST.get("txtdis") 
            toolstock = request.POST.get("txtstock") 
            toolamount = request.POST.get("txtamount") 
            toolstatus = request.POST.get("txtstatus") 
            toolsubcategory = request.POST.get("subcategory") 
            tooltype = request.POST.get("txttype")
            loginid = request.session.get("loginId")
            seller = tbl_seller.objects.get(seller_loginid__loginid = loginid)
            #return HttpResponse(seller)
            tob = tbl_tool()
            tob.tool_name = toolname  #cob.districtname(fieldname in table) = value (eg:cob.districtname=muscic)
            tob.tool_photo = toolimage
            tob.tool_discription = tooldiscription
            tob.tool_stock = toolstock
            tob.tool_price = toolamount
            tob.tool_status = "Available"
            tob.tool_subcategory = tbl_subcategory.objects.get(subcategory_id = toolsubcategory)
            tob.tool_type = tooltype
            tob.tool_seller = seller
            if tbl_tool.objects.filter(tool_subcategory = toolsubcategory,tool_name = toolname,tool_type = tooltype).exists():
                return HttpResponse("<script>alert('Alredy Exists..');window.location='/Seller/toolsRegistration/';</script>")
            else:
                tob.save() # insert query
                return HttpResponse("<script>alert('Sucessfuly inserted');window.location='/Seller/toolsRegistration';</script>")
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillsubcategory(request):
    loginid = request.session.get("loginId")
    if loginid:
        cid = int(request.POST.get("cid"))
        subcategory=tbl_subcategory.objects.filter(category_id=cid).values()#select * from tbl_subcategory
        return JsonResponse(list(subcategory),safe=False)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def toolsView(request):
    loginid = request.session.get("loginId")
    if loginid:
        category=tbl_category.objects.all()#select * from tbl_category
        return render(request,'Seller/toolsView.html',{ 'category': category})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def filltools1(request):
    loginid = request.session.get("loginId")
    if loginid:
        scid = int(request.POST.get("scid"))
        tool = request.POST.get("tid")
        loginid = request.session.get('loginId')
        sellerid = tbl_seller.objects.get(seller_loginid__loginid = loginid)
        # return HttpResponse(sellerid)
        tools=tbl_tool.objects.filter(tool_subcategory=scid,tool_type=tool,tool_seller=sellerid).values()#select * from tbl_tool
        return JsonResponse(list(tools),safe=False)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletetool(request,id):
    loginid = request.session.get("loginId")
    if loginid:
        lob=tbl_tool.objects.get(tool_id=id) 
        lob.delete()
        return HttpResponse("<script>alert('Sucessfuly Deleted');window.location='/Seller/toolsView';</script>")
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def requestView(request):
    loginid = request.session.get("loginId")
    if loginid:
        requestV = tbl_rentrequest.objects.select_related('request_toolid', 'request_userid').filter(request_Status = "Requested")
        return render(request, 'Seller/requestView.html', {'requestV': requestV})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def acceptRequest_process (request,id):
    loginid = request.session.get("loginId")
    if loginid:
        #return HttpResponse(seller)
        rob = tbl_rentrequest.objects.get(request_id = id)        
        if tbl_rentrequest.objects.filter(request_id = id,request_Status = "Accepted").exists():
            return HttpResponse("<script>alert('Alredy Accepted..');window.location='/Seller/requestView/';</script>")
        else:
            rob.request_Status = "Accepted"
            rob.save() # insert query
            return HttpResponse("<script>alert('Sucessfuly updated');window.location='/Seller/requestView';</script>")
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def rejectRequest_process (request,id):
    loginid = request.session.get("loginId")
    if loginid:
        rob = tbl_rentrequest.objects.get(request_id = id)     
        remark = request.POST.get("Remark")   
        if tbl_rentrequest.objects.filter(request_id = id,request_Status = "Rejected").exists():
            return HttpResponse("<script>alert('Alredy Rejected..');window.location='/Seller/requestView/';</script>")
        else:
            rob.request_Remark = remark
            rob.request_Status = "Rejected"
            rob.save() # insert query
            return HttpResponse("<script>alert('Sucessfuly updated');window.location='/Seller/requestView';</script>")
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")
   
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edittool(request, id):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == "POST":
            tob = tbl_tool.objects.get(tool_id=id)
            tob.tool_name = request.POST.get('txtname')
            tob.tool_discription = request.POST.get('txtdis')
            tob.tool_price = request.POST.get('price')
            tob.tool_type = request.POST.get('txttype')
            if len(request.FILES) != 0:
                tob.tool_photo = request.FILES['pimagenew']
            else:
                tob.tool_photo = request.POST.get('pimage')
            tob.save()
            return HttpResponse("<script>alert('Sucessfuly');window.location='/Seller/toolsView';</script>")
        else:
            tool = tbl_tool.objects.get(tool_id=id)
            return render(request, "Seller/toolsEdit.html", {'tool': tool})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def paymentView(request):
    loginid = request.session.get("loginId")
    if loginid:
        return render(request, 'Seller/paymentView.html',)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

def rentUpdate(request,id):
    loginid = request.session.get("loginId")
    if loginid:
        rpob = tbl_rentpayment.objects.get(rpayment_id=id)  
        rpob.rpayment_status = "Returned" 
        rpob.save() #update table
        return render(request, 'Seller/paymentView.html',)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillPurchasedOption(request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == "POST":
            purchased = tbl_purchasepayment.objects.filter( ppayment_purchaserequestid__purchase_toolid__tool_seller__seller_loginid = loginid).select_related(
                'ppayment_purchaserequestid', 'ppayment_userid', 'ppayment_purchaserequestid__purchase_toolid'
            ).values(
                'ppayment_id',
                'ppayment_purchaserequestid__purchase_toolid__tool_name',
                'ppayment_purchaserequestid__purchase_toolid__tool_photo',
                'ppayment_date',
                'ppayment_amount',
                'ppayment_userid__user_name'
            )

            return JsonResponse(list(purchased), safe=False)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillRentedOption(request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == "POST":
            rented = tbl_rentpayment.objects.filter( rpayment_status="Paid",rpayment_rentrequestid__request_toolid__tool_seller__seller_loginid = loginid).select_related(
                'rpayment_rentrequestid', 'rpayment_userid', 'rpayment_rentrequestid__request_toolid'
            ).values(
                'rpayment_id',
                'rpayment_rentrequestid__request_toolid__tool_name',
                'rpayment_rentrequestid__request_toolid__tool_photo',
                'rpayment_date',
                'rpayment_amount',
                'rpayment_userid__user_name',
                'rpayment_rentrequestid__request_requireddate',
                'rpayment_rentrequestid__request_returndate'
            )

            return JsonResponse(list(rented), safe=False)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profileView(request,id):
    loginid = request.session.get("loginId")
    if loginid:
        seller=tbl_seller.objects.get(seller_id = id)#select * from tbl_category
        return render(request,'Seller/profileView.html',{ 'seller': seller})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profileEdit(request,id):
    loginid = request.session.get("loginId")
    if loginid:
        seller=tbl_seller.objects.get(seller_id = id)#select * from tbl_category
        districts=tbl_district.objects.all()#select * from tbl_district
        return render(request,'Seller/profileEdit.html',{ 'seller': seller,'districts': districts})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editprofile(request, id):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == "POST":
            sob = tbl_seller.objects.get(seller_id=id)
            sob.seller_name = request.POST.get('txtname')
            sob.seller_email = request.POST.get('txtdis')
            sob.seller_phone = request.POST.get('phone')
            sob.seller_landmark = request.POST.get('Landmark')
            sob.seller_pincode = request.POST.get('pincode')
            location = request.POST.get("location")
            sob.seller_location = tbl_location.objects.get(location_id=location)
            if len(request.FILES) != 0:
                sob.seller_image = request.FILES['pimagenew']
            else:
                sob.seller_image = request.POST.get('pimage')
            sob.save()
            return HttpResponse("<script>alert('Sucessfuly');window.location='/Seller/Sellerhome/';</script>")
        else:
            seller = tbl_seller.objects.get(seller_id=id)
            return render(request, "Seller/profileEdit.html", {'seller': seller})
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def filllocation(request):
    loginid = request.session.get("loginId")
    if loginid:
        did = int(request.POST.get("did"))
        location=tbl_location.objects.filter(district_id=did).values()#select * from tbl_location
        return JsonResponse(list(location),safe=False)
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

#Excel Export Code

class ExportExcelToolRent(View):
    def get(self, request, option):
        loginid = request.session.get("loginId")
        if loginid:
            # return HttpResponse(option)
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="ToolRentlist.xls"'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Sheet1')

            # Define the column headings
            row_num = 0
            # Query the data from your model, and write it to the worksheet
            if(option == "Rented"):
                columns = ['Tools Name', 'Paymount date', 'Amount', 'Customer name', 'Rent From Date','Rent To Date']
                for col_num, column_title in enumerate(columns):
                    ws.write(row_num, col_num, column_title)
                queryset = tbl_rentpayment.objects.filter( rpayment_rentrequestid__request_toolid__tool_seller__seller_loginid = loginid).values_list(
                'rpayment_rentrequestid__request_toolid__tool_name',
                'rpayment_date',
                'rpayment_amount',
                'rpayment_userid__user_name',
                'rpayment_rentrequestid__request_requireddate',
                'rpayment_rentrequestid__request_returndate')
                
            if(option == "Purchased"):
                columns = ['Tools Name', 'Paymount date', 'Amount', 'Customer name']
                for col_num, column_title in enumerate(columns):
                    ws.write(row_num, col_num, column_title)
                queryset = tbl_purchasepayment.objects.filter( ppayment_purchaserequestid__purchase_toolid__tool_seller__seller_loginid = loginid).values_list(
                'ppayment_purchaserequestid__purchase_toolid__tool_name',
                'ppayment_date',
                'ppayment_amount',
                'ppayment_userid__user_name')
            
            for row in queryset:
                row_num += 1
                for col_num, cell_value in enumerate(row):
                    ws.write(row_num, col_num, cell_value)

            wb.save(response)
            return response
        else:
            return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


# End of excel export code

# pie chart departmentbased student

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pie_chart(request):
    loginid = request.session.get("loginId")
    if loginid:
        queryset = tbl_rentrequest.objects.values('request_toolid__tool_name').annotate(total_tools=Count('request_id'))
        
        labels = [entry['request_toolid__tool_name'] for entry in queryset]
        data = [entry['total_tools'] for entry in queryset]

        return render(request, 'Seller/piechartRentTools.html', {
            'labels': labels,
            'data': data,
        })
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pie_chart_purchased(request):
    loginid = request.session.get("loginId")
    if loginid:
        queryset = tbl_purchaserequest.objects.values('purchase_toolid__tool_name').annotate(total_tools=Count('purchase_id'))
        
        labels = list(queryset.values_list('purchase_toolid__tool_name', flat=True))  # Ensuring list format
        data = list(queryset.values_list('total_tools', flat=True))  # Ensuring integers

        return render(request, 'Seller/piechartRentTools.html', {
            'labels': labels,
            'data': data,
        })
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
def placed (request,id):
    loginid = request.session.get("loginId")
    if loginid:
        rob = tbl_purchasepayment.objects.get(ppayment_id = id)     
        if tbl_purchasepayment.objects.filter(ppayment_id = id,ppayment_status = "placed").exists():
            return HttpResponse("<script>alert('Alredy Updated..');window.location='/Seller/paymentView';</script>")
        else:
            rob.ppayment_status = "placed"
            rob.save() # insert query
            return HttpResponse("<script>alert('Sucessfuly updated');window.location='/Seller/paymentView';</script>")
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def transit (request,id):
    loginid = request.session.get("loginId")
    if loginid:
        rob = tbl_purchasepayment.objects.get(ppayment_id = id)     
        if tbl_purchasepayment.objects.filter(ppayment_id = id,ppayment_status = "transit").exists():
            return HttpResponse("<script>alert('Alredy Updated..');window.location='/Seller/paymentView';</script>")
        else:
            rob.ppayment_status = "transit"
            rob.save() # insert query
            return HttpResponse("<script>alert('Sucessfuly updated');window.location='/Seller/paymentView';</script>")
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def for_delivery (request,id):
    loginid = request.session.get("loginId")
    if loginid:
        rob = tbl_purchasepayment.objects.get(ppayment_id = id)     
        if tbl_purchasepayment.objects.filter(ppayment_id = id,ppayment_status = "for_delivery").exists():
            return HttpResponse("<script>alert('Alredy Updated..');window.location='/Seller/paymentView';</script>")
        else:
            rob.ppayment_status = "for_delivery"
            rob.save() # insert query
            return HttpResponse("<script>alert('Sucessfuly updated');window.location='/Seller/paymentView';</script>")
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delivered (request,id):
    loginid = request.session.get("loginId")
    if loginid:
        rob = tbl_purchasepayment.objects.get(ppayment_id = id)     
        if tbl_purchasepayment.objects.filter(ppayment_id = id,ppayment_status = "delivered").exists():
            return HttpResponse("<script>alert('Alredy Updated..');window.location='/Seller/paymentView';</script>")
        else:
            rob.ppayment_status = "delivered"
            rob.save() # insert query
            return HttpResponse("<script>alert('Sucessfuly updated');window.location='/Seller/paymentView';</script>")
    else:
       return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

# Create your views here.
