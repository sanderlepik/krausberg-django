from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

def home(request):
    template_name = 'index.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)

            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})

        else:
            #TODO
            error_msg = "Form contains errors!"
            return render(request, template_name, {'contact_form': contact_form})


def services(request):
    template_name = 'services.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)

            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})

        else:
            #TODO
            error_msg = "Form contains errors!"
            return render(request, template_name, {'contact_form': contact_form})


def service(request):
    template_name = 'service.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)

            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})

        else:
            #TODO
            error_msg = "Form contains errors!"
            return render(request, template_name, {'contact_form': contact_form})


def job_offer(request):
    template_name = 'job-offers.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)

            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})

        else:
            #TODO
            error_msg = "Form contains errors!"
            return render(request, template_name, {'contact_form': contact_form})


def contact(request):
    template_name = 'contact.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)

            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})

        else:
            #TODO
            error_msg = "Form contains errors!"
            return render(request, template_name, {'contact_form': contact_form})


def business(request):
    template_name = 'business.html'
    contact_form = ContactForm()

    if request.method == 'GET':
        return render(request, template_name, {'contact_form': contact_form})

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone_num = contact_form.cleaned_data['phone_num']
            email = contact_form.cleaned_data['email']
            address = contact_form.cleaned_data['address']
            message = contact_form.cleaned_data['message']

            ctx = {'name': name, 'phone_num': phone_num, 'email': email, 'address': address, 'message': message}
            message = render_to_string('contact-template.txt', ctx)

            send_mail(subject='Krausberg veeb - kontakt', message=message, from_email=email, recipient_list = ['sander.lepik@knowit.ee'])

            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})

        else:
            #TODO
            error_msg = "Form contains errors!"
            return render(request, template_name, {'contact_form': contact_form})