from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import pytz
from django.views.decorators.cache import cache_page
from pytz import UnknownTimeZoneError
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import RequestLog


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@cache_page(200)
def main_page(request: HttpRequest) -> HttpResponse:
    log, _ = RequestLog.objects.get_or_create(user_agent=request.META.get('HTTP_USER_AGENT', None), ip=get_client_ip(request))
    log.visits += 1
    log.save()
    return render(request, 'main.html')


@api_view(['GET'])
def visits(request: Request) -> Response:
    logs = RequestLog.objects.all().order_by("-visits")[:100]
    data = list(map(lambda l: {"ip": l.ip, "UserAgent": l.user_agent, "visits": l.visits}, logs))
    return Response(data=data)

@api_view(['GET'])
def time(request: Request) -> Response:
    zone = request.query_params.get('timezone', 'Europe/Moscow')
    try:
        tz = pytz.timezone(zone)
    except UnknownTimeZoneError:
        return Response(status=400, data={"timezone": "Unknown timezone"})
    moscow_time_now = datetime.now(tz)
    return Response(data={"datetime": moscow_time_now.isoformat(), 'timezone': zone})
