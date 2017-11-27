from django.shortcuts import render

def home(request):
    template_name = 'index.html'
    return render(request, template_name)

def services(request):
    template_name = 'services.html'
    return render(request, template_name)

def service(request):
    template_name = 'service.html'
    return render(request, template_name)

def job_offer(request):
    template_name = 'job-offers.html'
    return render(request, template_name)

def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)

def business(request):
    template_name = 'business.html'
    return render(request, template_name)