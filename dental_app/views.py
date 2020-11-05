from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'dental_app/home.html', {})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #Send Email to the address
        send_mail(
            message_name, #subject
            message_email, #From Address
            message, #message
            ['refugedesigns17@gmail.com'], #to email
            fail_silently=True
        )
    return render(request, 'dental_app/contact.html', {})

def about(request):
    return render(request, 'dental_app/about.html', {})

def blog(request):
    return render(request, 'dental_app/blog.html', {})

def book(request):
    return render(request, 'dental_app/book.html', {})

def pricing(request):
    return render(request, 'dental_app/pricing.html', {})

def service(request):
    return render(request, 'dental_app/service.html', {})

def blog_details(request):
    return render(request, 'dental_app/blog-details.html', {})