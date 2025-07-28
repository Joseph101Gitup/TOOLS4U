from django.urls import path
from AdminApp import views


urlpatterns = [
path('Adminhome/',views.Adminhome),
path('district/',views.district,name='district'),
path('district_process/',views.district_process,name="district_process"),
path('location/',views.location,name='location'),
path('location_process/',views.location_process,name="location_process"),
path('category/',views.category,name='category'),
path('category_process/',views.category_process,name="category_process"),
path('subcategory/',views.subcategory,name='subcategory'),
path('subcategory_process/',views.subcategory_process,name="subcategory_process"),
path('districtview/',views.districtview,name='districtview'),
path('locationview/',views.locationview,name='locationview'),
path('filllocation/',views.filllocation,name='filllocation'),
path('deletelocation/<did>',views.deletelocation,name='deletelocation'), 
path('categoryview/',views.categoryview,name='categoryview'),
path('deletecategory/<categoryid>',views.deletecategory,name='deletecategory'),  
path('subcategoryview/',views.subcategoryview,name='subcategoryview'),
path('fillSubcategory/',views.fillSubcategory,name='fillSubcategory'),
path('deletesubcategory/<subcategoryid>',views.deletesubcategory,name='deletesubcategory'),  
path('sellerview/',views.sellerview,name='sellerview'),
path('sellerAccept/<loginid>',views.sellerAccept,name='sellerAccept'),
path('sellerReject/<loginid>',views.sellerReject,name='sellerReject'),
path('categoryEdit/<categoryid>',views.categoryEdit,name='categoryEdit'),
path('subCategoryEdit/<subcategoryid>',views.subCategoryEdit,name='subCategoryEdit'),
path('allsellerview/',views.allSellerView,name='allsellerview'),
path('adminPaymentView',views.adminPaymentView,name='adminPaymentView'),  
path('AdminfillPurchasedOption/',views.AdminfillPurchasedOption,name='AdminfillPurchasedOption'),
path('AdminfillRentedOptions/',views.AdminfillRentedOptions,name='AdminfillRentedOptions'),
path('Adminexport_excel/<option>',views.ExportExcelToolRent.as_view(), name='Adminexport_excel'),
path('logout/',views.logout,name='logout'),
path('IndexA/',views.IndexA,name="IndexA"),



]