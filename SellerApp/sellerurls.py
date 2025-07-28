from django.urls import path
from SellerApp import views


urlpatterns = [
path('Sellerhome/',views.Sellerhome,name='Sellerhome'),
path('toolsRegistration/',views.toolsRegistration,name='toolsRegistration'),
path('toolsRegistration_process/',views.toolsRegistration_process,name='toolsRegistration_process'),
path('fillsubcategory/',views.fillsubcategory,name='fillsubcategory'),
path('toolsView/',views.toolsView,name='toolsView'),
path('filltools1/',views.filltools1,name='filltools1'),
path('deletetool/<id>',views.deletetool,name='deletetool'),  
path('requestView',views.requestView,name='requestView'),  
path('acceptRequest_process/<id>',views.acceptRequest_process,name='acceptRequest_process'),  
path('rejectRequest_process/<id>',views.rejectRequest_process,name='rejectRequest_process'),  
path('edittool/<id>',views.edittool,name='edittool'),  
path('paymentView',views.paymentView,name='paymentView'),  
path('rentUpdate/<id>',views.rentUpdate,name='rentUpdate'),  
path('fillPurchasedOption/',views.fillPurchasedOption,name='fillPurchasedOption'),
path('fillRentedOption/',views.fillRentedOption,name='fillRentedOption'),
path('profileView/<id>',views.profileView,name='profileView'),
path('export_excel/<option>',views.ExportExcelToolRent.as_view(), name='export_excel'),
path('pie_chart_rent/',views.pie_chart,name='pie_chart_rent'),
path('pie_chart_purchased/',views.pie_chart_purchased,name='pie_chart_purchased'),
path('profileEdit/<id>',views.profileEdit,name='profileEdit'),
path('editprofile/<id>',views.editprofile,name='editprofile'),  
path('filllocation/',views.filllocation,name='filllocation'),
path('logout/',views.logout,name='logout'),
path('placed/<id>',views.placed,name='placed'), 
path('transit/<id>',views.transit,name='transit'), 
path('for_delivery/<id>',views.for_delivery,name='for_delivery'),
path('delivered/<id>',views.delivered,name='delivered'),
]