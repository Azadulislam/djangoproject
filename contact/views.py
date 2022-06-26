import email
from email import message

from django.shortcuts import render

from contact.models import Contact


# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get("message")

        Contact(name=name, email=email, subject=subject, message=message).save()

    return render(request, 'contact.html')
