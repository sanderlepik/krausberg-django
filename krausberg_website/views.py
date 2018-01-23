from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import JobOffer


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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def job_offer(request):
    template_name = 'job-offers.html'
    contact_form = ContactForm()

    active_offers = JobOffer.objects.all()

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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def private(request):
    template_name = 'private.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def administrator(request):
    template_name = 'administrator.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_1(request):
    template_name = 'service-1.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_2(request):
    template_name = 'service-2.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_3(request):
    template_name = 'service-3.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_4(request):
    template_name = 'service-4.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_5(request):
    template_name = 'service-5.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_6(request):
    template_name = 'service-6.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_7(request):
    template_name = 'service-7.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_8(request):
    template_name = 'service-8.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_9(request):
    template_name = 'service-9.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_10(request):
    template_name = 'service-10.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_11(request):
    template_name = 'service-11.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_12(request):
    template_name = 'service-12.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_13(request):
    template_name = 'service-13.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_14(request):
    template_name = 'service-14.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_15(request):
    template_name = 'service-15.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def service_16(request):
    template_name = 'service-16.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})


def about_us(request):
    template_name = 'about-us.html'
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
            send_mail(subject='Krausberg veeb - kontakt',
                      message=message,
                      from_email='krausberg@krausberg.ee',
                      recipient_list=['krausberg@krausberg.ee'])

            # Initializing empty form after sending email
            contact_form = ContactForm()

            return render(request, template_name, {'contact_form': contact_form})

        else:
            contact_form = ContactForm()
            return render(request, template_name, {'contact_form': contact_form})