from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import job_offers

def home(request):
    template_name = 'index.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():

            # Getting data from django contact form
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            # Sending email
            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)
            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def services(request):
    template_name = 'services.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():

            # Getting data from django contact form
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            # Sending email
            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)
            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service(request):
    template_name = 'service.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():

            # Getting data from django contact form
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            # Sending email
            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)
            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def job_offer(request):
    template_name = 'job-offers.html'
    contact_form = ContactForm()

    active_offers = job_offers.objects.all()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form, 'active_offers': active_offers})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():

            # Getting data from django contact form
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            # Sending email
            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)
            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form, 'active_offers': active_offers})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form, 'active_offers': active_offers})


def contact(request):
    template_name = 'contact.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():

            # Getting data from django contact form
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            # Sending email
            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)
            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def business(request):
    template_name = 'business.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():

            # Getting data from django contact form
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            # Sending email
            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)
            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})