from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignUpForm, ContactForm

# Create your views here.


def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form
    }
    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_fullname = form.cleaned_data.get("fullname")
        form_message = form.cleaned_data.get("message")
        subject = "Site Contact Form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'ochiengogori@gmail.com', 'ogoridavis@gmail.com']
        contact_msg = """
         %s: %s  via %s
        """%(form_fullname, form_message, form_email)
        send_mail(subject, contact_msg, from_email, to_email, html_message="""<h1>hello</h1>""" ,fail_silently=False)
    context = {
        "form": form
    }
    return render(request, "contact.html", context)


def about(request):
    context = {

    }
    return render(request, "about.html", context)
