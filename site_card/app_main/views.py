from django.shortcuts import render
from django.conf import settings


def get_contact_context():
    return {
        'contact_phone': settings.PHONE,
        'contact_email': settings.EMAIL,
        'contact_telegram': settings.TELEGRAM_USERNAME,
        'contact_viber': settings.VIBER_PHONE
    }


def home(request):
    # return render(request, 'app_main/home.html', get_contact_context())
    return render(request, 'app_main/home.html')


def about(request):
    # print(get_contact_context())
    # return render(request, 'app_main/about.html', get_contact_context())
    return render(request, 'app_main/about.html')


def services(request):
    # print(get_contact_context())
    # return render(request, 'app_main/services.html', get_contact_context())
    return render(request, 'app_main/services.html')


def faq(request):
    # print(get_contact_context())
    # return render(request, 'app_main/faq.html', get_contact_context())
    return render(request, 'app_main/faq.html')
