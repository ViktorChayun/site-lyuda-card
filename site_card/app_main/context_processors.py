from django.conf import settings


def contact_info(request):
    return {
        'contact_phone': settings.PHONE,
        'contact_email': settings.EMAIL,
        'contact_telegram': settings.TELEGRAM_USERNAME,
        'contact_viber': settings.VIBER_PHONE
    }
