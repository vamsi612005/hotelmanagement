from django.shortcuts import render
from hotel.models import hoteldetails
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.
def test(request):
    return render(request,'usert/test.html')


def userviewhotel(request):
    hotels = hoteldetails.objects.all()
    return render(request, 'usert/userviewhotel.html', {'hotels': hotels})


def userhome(request):
    return render(request, 'usert/userhome.html')


def userviewprofile(request):
    return render(request, 'usert/userviewprofile.html',)


def useraddemail(request):
    if request.method == "POST":
        email = request.POST.get('emailu')
        cuser = request.user
        cuser.email=email
        cuser.save()
        return render(request,'usert/userviewprofile.html')


def useraddfirstname(request):
    if request.method == "POST":
        email = request.POST.get('firstnameu')
        cuser = request.user
        print(cuser.email)
        cuser.first_name=email
        cuser.save()
        return render(request,'usert/userviewprofile.html')


def useraddlastname(request):
    if request.method == "POST":
        email = request.POST.get('lastnameu')
        cuser = request.user
        print(cuser.email)
        cuser.last_name=email
        cuser.save()
        return render(request,'usert/userviewprofile.html')


def bookaroom(request):
    return render(request, 'usert/bookaroom.html')


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        recipient_email = '2200031906cseh@gmail.com'
        subject = 'This feedback is from ' + name + 'bearing the email id' + email
        message_body = message
        send_mail(
            subject,
            message_body,
            '2200031906cseh@gmail.com',
            [recipient_email],
            fail_silently=False,
        )
        return render(request,'usert/contactus.html')
    else:
        return render(request,'usert/contactus.html')

