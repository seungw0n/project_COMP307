from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            to_email = [settings.EMAIL_HOST_USER,]
            try:
                send_mail(subject, message,from_email,recipient_email, fail_silently=False)
                send_mail("LOOK-N-FIT", "Thank you for contacting us!", settings.EMAIL_HOST_USER, [from_email], fail_silently=False)
            except:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "contactus.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for contacting us!')
