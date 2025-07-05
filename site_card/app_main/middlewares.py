import geoip2.database
from .models import VisitLog
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import logging


logger = logging.getLogger(__name__)


class VisitorLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        path = request.path

        # GeoIP2 – необов’язково (якщо хочеш геолокацію)
        country, city = None, None
        try:
            reader = geoip2.database.Reader(settings.GEOLITE_FILE)
            response = reader.city(ip)
            country = response.country.name
            city = response.city.name
        except Exception as err:
            logger.warning(f"error geoip2 - {err}")

        VisitLog.objects.create(
            ip_address=ip,
            user_agent=user_agent,
            path=path,
            country=country,
            city=city
        )


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
