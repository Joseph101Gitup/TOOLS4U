from django.db.models import Count
from django.shortcuts import redirect, render
from AdminApp.models import tbl_district,tbl_location,tbl_category,tbl_subcategory
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_control

from GuestApp.models import tbl_login, tbl_seller, tbl_user
from SellerApp.models import tbl_tool
from UserApp.models import tbl_purchasepayment, tbl_rentpayment

import xlwt
from django.views.generic import View

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Adminhome(request):
    loginid = request.session.get("loginId")
    if loginid:
        tools=tbl_tool.objects.count()#select * from tbl_tool
        seller=tbl_seller.objects.count()#select * from tbl_seller
        Coustomers=tbl_user.objects.count()#select * from tbl_user
        return render(request,'Admin/index.html',{ 'tools': tools,'seller': seller,'Coustomers': Coustomers})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def district(request):
    loginid = request.session.get("loginId")
    if loginid:
        return render(request,'Admin/district.html')
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def district_process (request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == 'POST':
            districtname = request.POST.get("districtname")     #textboxname = music
            dob = tbl_district()
            dob.district_name = districtname  #cob.districtname(fieldname in table) = value (eg:cob.districtname=muscic)
            if tbl_district.objects.filter(district_name=districtname).exists():
                return HttpResponse("<script>alert('Alredy Exists..');window.location='/Admin/district.html';</script>")
            else:
                dob.save() # insert query
                return HttpResponse("<script>alert('Sucessfuly inserted');window.location='/Admin/district.html';</script>")
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def location(request):
    loginid = request.session.get("loginId")
    if loginid:
        districts=tbl_district.objects.all()#select * from tbl_district
        return render(request,'Admin/location.html',{ 'districts': districts})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def location_process (request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == 'POST':
            districtid = request.POST.get("districtid")    #textboxname = music
            lname= request.POST.get("locationname")
            lob = tbl_location()
            lob.location_name = lname  #cob.districtname(fieldname in table) = value (eg:cob.districtname=muscic)
            lob.district_id = tbl_district.objects.get(district_id=districtid)
            if tbl_location.objects.filter(location_name=lname,district_id=districtid).exists():
                return HttpResponse("<script>alert('Alredy Exists..');window.location='/Admin/location';</script>")
            else:
                lob.save() # insert query
                return HttpResponse("<script>alert('Sucessfuly inserted');window.location='/Admin/location';</script>")
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

            
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def category(request):
    loginid = request.session.get("loginId")
    if loginid:
        return render(request,'Admin/category.html')
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def category_process (request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == 'POST':
            categoryname = request.POST.get("categoryname")     #textboxname = music
            categoryimage = request.FILES["categoryimage"]
            cob = tbl_category()
            cob.category_name = categoryname  #cob.districtname(fieldname in table) = value (eg:cob.districtname=muscic)
            cob.category_image=categoryimage
            if tbl_category.objects.filter(category_name=categoryname).exists():
                return HttpResponse("<script>alert('Alredy Exists..');window.location='/Admin/category/';</script>")
            else:
                cob.save() # insert query
                return HttpResponse("<script>alert('Sucessfuly inserted');window.location='/Admin/category';</script>")
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

            
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subcategory(request):
    loginid = request.session.get("loginId")
    if loginid:
        category=tbl_category.objects.all()#select * from tbl_category
        return render(request,'Admin/subCategory.html',{ 'category': category})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subcategory_process (request):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == 'POST':
            categoryid = request.POST.get("categoryid")    #textboxname = music
            scname= request.POST.get("subcategoryname")
            scimage = request.FILES["subcategoryimage"]
            scob = tbl_subcategory()
            scob.subcategory_name = scname  #cob.districtname(fieldname in table) = value (eg:cob.districtname=muscic)
            scob.category_id = tbl_category.objects.get(category_id=categoryid)
            scob.subcategory_image=scimage
            if tbl_subcategory.objects.filter(subcategory_name=scname,category_id=categoryid).exists():
                return HttpResponse("<script>alert('Alredy Exists..');window.location='/Admin/subcategory';</script>")
            else:
                scob.save() # insert query
                return HttpResponse("<script>alert('Sucessfuly inserted');window.location='/Admin/subcategory';</script>")
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def districtview(request):
    loginid = request.session.get("loginId")
    if loginid:
        district=tbl_district.objects.all()#select * from tbl_district
        return render(request,'Admin/districtView.html',{ 'district': district})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def locationview(request):
    loginid = request.session.get("loginId")
    if loginid:
        district=tbl_district.objects.all()#select * from tbl_district
        return render(request,'Admin/locationview.html',{ 'district': district})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def filllocation(request):
    loginid = request.session.get("loginId")
    if loginid:
        did = int(request.POST.get("did"))
        location=tbl_location.objects.filter(district_id=did).values()#select * from tbl_district
        return JsonResponse(list(location),safe=False)
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletelocation(request,did):
    loginid = request.session.get("loginId")
    if loginid:
        lob=tbl_location.objects.get(location_id=did) 
        lob.delete()
        return HttpResponse("<script>alert('Sucessfuly Deleted');window.location='/Admin/locationView';</script>")
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def categoryview(request):
    loginid = request.session.get("loginId")
    if loginid:
        category=tbl_category.objects.all()#select * from tbl_category
        return render(request,'Admin/categoryView.html',{ 'category': category})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletecategory(request,categoryid):
    loginid = request.session.get("loginId")
    if loginid:
        cob=tbl_category.objects.get(category_id=categoryid) 
        cob.delete()
        return HttpResponse("<script>alert('Sucessfuly Deleted');window.location='/Admin/categoryView';</script>")
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subcategoryview(request):
    loginid = request.session.get("loginId")
    if loginid:
        category=tbl_category.objects.all()#select * from tbl_category
        return render(request,'Admin/subCategoryView.html',{ 'category': category})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillSubcategory(request):
    loginid = request.session.get("loginId")
    if loginid:
        cid = int(request.POST.get("cid"))
        subcategory=tbl_subcategory.objects.filter(category_id=cid).values()#select * from tbl_subcategory
        return JsonResponse(list(subcategory),safe=False)
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletesubcategory(request,subcategoryid):
    loginid = request.session.get("loginId")
    if loginid:
        scob=tbl_subcategory.objects.get(subcategory_id=subcategoryid) 
        scob.delete()
        return HttpResponse("<script>alert('Sucessfuly Deleted');window.location='/Admin/subCategoryView';</script>")
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sellerview(request):
    loginid = request.session.get("loginId")
    if loginid:
        seller=tbl_seller.objects.filter(seller_loginid__status="Requested").values('seller_location__location_name','seller_name','seller_image','seller_phone','seller_email','seller_idproof','seller_regdate','seller_loginid__loginid')
        return render(request,'Admin/sellerView.html',{ 'seller': seller})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sellerAccept(request,loginid):
    loginid = request.session.get("loginId")
    if loginid:
        lob=tbl_login.objects.get(loginid=loginid)
        lob.status = "Accepted"
        lob.save()
        return HttpResponse("<script>alert('Accepted...');window.location='/Admin/sellerview/';</script>")
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sellerReject(request,loginid):
    loginid = request.session.get("loginId")
    if loginid:
        lob=tbl_login.objects.get(loginid=loginid)
        lob.status = "Rejected"
        lob.save()
        return HttpResponse("<script>alert('Rejected...');window.location='/Admin/sellerview/';</script>")
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def categoryEdit(request,categoryid):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == "POST":
            cob = tbl_category.objects.get(category_id=categoryid)
            cob.category_name = request.POST.get('categoryname')
            if len(request.FILES) != 0:
                cob.category_image = request.FILES['pimagenew']
            else:
                cob.category_image = request.POST.get('pimage')
            cob.save()
            return HttpResponse("<script>alert('Sucessfuly');window.location='/Admin/categoryview/';</script>")
        else:
            category = tbl_category.objects.get(category_id=categoryid)
            return render(request, "Admin/categoryEdit.html", {'category': category})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subCategoryEdit(request,subcategoryid):
    loginid = request.session.get("loginId")
    if loginid:
        if request.method == "POST":
            scob = tbl_subcategory.objects.get(subcategory_id=subcategoryid)
            scob.subcategory_name = request.POST.get('subcategoryname')
            if len(request.FILES) != 0:
                scob.subcategory_image = request.FILES['pimagenew']
            else:
                scob.subcategory_image = request.POST.get('pimage')
            scob.save()
            return HttpResponse("<script>alert('Sucessfuly');window.location='/Admin/subcategoryview/';</script>")
        else:
            subcategory = tbl_subcategory.objects.get(subcategory_id=subcategoryid)
            return render(request, "Admin/subCategoryEdit.html", {'subcategory': subcategory})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def allSellerView(request):
    loginid = request.session.get("loginId")
    if loginid:
        seller=tbl_seller.objects.filter(seller_loginid__status="Accepted").values('seller_location__location_name','seller_name','seller_image','seller_phone','seller_email','seller_idproof','seller_regdate','seller_loginid__loginid')
        return render(request,'Admin/allSellerView.html',{ 'seller': seller})
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminPaymentView(request):
    loginid = request.session.get("loginId")
    if loginid:
        return render(request, 'Admin/adminPaymentView.html',)
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def AdminfillPurchasedOption(request):
    loginid = request.session.get("loginId")
    if loginid:
        year= request.POST.get('year')
        purchased = tbl_purchasepayment.objects.filter(ppayment_date__year=year).select_related(
                'ppayment_purchaserequestid', 'ppayment_userid', 'ppayment_purchaserequestid__purchase_toolid', 'ppayment_purchaserequestid__purchase_toolid__tool_seller'
            ).values(
                'ppayment_purchaserequestid__purchase_toolid__tool_name',
                'ppayment_purchaserequestid__purchase_toolid__tool_photo',
                'ppayment_date',
                'ppayment_amount',
                'ppayment_userid__user_name',
                'ppayment_purchaserequestid__purchase_toolid__tool_seller__seller_name'
            )

        return JsonResponse(list(purchased), safe=False)
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def AdminfillRentedOptions(request):
    loginid = request.session.get("loginId")
    if loginid:
        year= request.POST.get('year')
        rented = tbl_rentpayment.objects.filter(rpayment_date__year=year).select_related(
            'rpayment_rentrequestid', 
            'rpayment_userid', 
            'rpayment_rentrequestid__request_toolid', 
            'rpayment_rentrequestid__request_toolid__tool_seller'
        ).values(
            'rpayment_rentrequestid__request_toolid__tool_name',
            'rpayment_rentrequestid__request_toolid__tool_photo',
            'rpayment_date',
            'rpayment_amount',
            'rpayment_userid__user_name',
            'rpayment_rentrequestid__request_toolid__tool_seller__seller_name', 
            'rpayment_rentrequestid__request_requireddate',
            'rpayment_rentrequestid__request_returndate'
        )

        return JsonResponse(list(rented), safe=False)
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


#Excel Export Code
class ExportExcelToolRent(View):
    def get(self, request, option):
            # return HttpResponse(option)
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="ToolRentlist.xls"'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Sheet1')

#define the column headings
            row_num = 0
            # Query the data from your model, and write it to the worksheet
            if(option == "Rented"):
                columns = ['Tools Name', 'Paymount date', 'Amount', 'Customer name','Seller name', 'Rent From Date','Rent To Date']
                for col_num, column_title in enumerate(columns):
                    ws.write(row_num, col_num, column_title)
                queryset = tbl_rentpayment.objects.all().values_list(
                'rpayment_rentrequestid__request_toolid__tool_name',
                'rpayment_date',
                'rpayment_amount',
                'rpayment_userid__user_name',
                'rpayment_rentrequestid__request_toolid__tool_seller__seller_name', 
                'rpayment_rentrequestid__request_requireddate',
                'rpayment_rentrequestid__request_returndate')
                
            if(option == "Purchased"):
                columns = ['Tools Name', 'Paymount date', 'Amount', 'Customer name','Seller name']
                for col_num, column_title in enumerate(columns):
                    ws.write(row_num, col_num, column_title)
                queryset = tbl_purchasepayment.objects.all().values_list(
                'ppayment_purchaserequestid__purchase_toolid__tool_name',
                'ppayment_date',
                'ppayment_amount',
                'ppayment_userid__user_name',
                'ppayment_purchaserequestid__purchase_toolid__tool_seller__seller_name')
            
            for row in queryset:
                row_num += 1
                for col_num, cell_value in enumerate(row):
                    ws.write(row_num, col_num, cell_value)

            wb.save(response)
            return response

# End of excel export code
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    loginid = request.session.get("loginId")
    if loginid:    
        request.session.clear()  #clears session variable only
        return redirect('/')
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def IndexA(request):
    loginid = request.session.get("loginId")
    if loginid:
        return render(request, 'Admin/Index.html',)
    else:
        return HttpResponse("<script>alert('Authentication required.....');window.location='/Login/';</script>")


# Create your views here.
