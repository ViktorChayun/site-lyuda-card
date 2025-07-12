from django.conf import settings


def contact_info(request):
    return {
        'contact_phone': getattr(settings, 'PHONE', ''),
        'contact_email': getattr(settings, 'EMAIL', ''),
        'contact_telegram': getattr(settings, 'TELEGRAM_USERNAME', ''),
        'contact_viber': getattr(settings, 'VIBER_PHONE', ''),
    }
