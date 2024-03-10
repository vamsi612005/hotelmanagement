from django.urls import path
from . import views

urlpatterns = [
    path('test',views.test,name='test'),
    path('',views.userhome,name='userhome'),
    path('userviewhotel',views.userviewhotel,name='userviewhotel'),
    path('userviewprofile',views.userviewprofile,name='userviewprofile'),
    path('useraddemail',views.useraddemail,name='useraddemail'),
    path('useraddfirstname',views.useraddfirstname,name='useraddfirstname'),
    path('useraddlastname',views.useraddlastname,name='useraddlastname'),
    path('bookaroom',views.bookaroom,name='bookaroom'),
    path('contactus',views.contactus,name='contactus'),
]