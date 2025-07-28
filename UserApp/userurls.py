from django.urls import path
from UserApp import views

urlpatterns = [
path('index/',views.index,name='index'),
path('Userhome/',views.Userhome,name='Userhome'),
path('filltools/',views.filltools,name='filltools'),
path('producturl/<id>/<type1>/', views.producturl, name='producturl'),
path('productRent/',views.productRent,name='productRent'),
path('payment_process/',views.payment_process,name='payment_process'),
path('rentedProductsView/',views.rentedProductsView,name='rentedProductsView'),
path('fillRequestedOption/',views.fillRequestedOption,name='fillRequestedOption'),
path('fillAcceptedOption/',views.fillAcceptedOption,name='fillAcceptedOption'),
path('fillRejectedOption/',views.fillRejectedOption,name='fillRejectedOption'),
path('fillPaidOption/',views.fillPaidOption,name='fillPaidOption'),
path('rentPayment/<id>',views.rentPayment,name='rentPayment'),
path('rentPayment_process/',views.rentPayment_process,name='rentPayment_process'),
path('purchasedProductView/',views.purchasedProductView,name='purchasedProductView'),
path('logout/',views.logout,name='logout'),
path('packageTracking/<id>',views.packageTracking,name='packageTracking'),
path('contactU/',views.contactU,name="contactU"),



]