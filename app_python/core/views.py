from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import pytz
from django.views.decorators.cache import cache_page
from pytz import UnknownTimeZoneError
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@cache_page(200)
def main_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'main.html')


@api_view(['GET'])
def time(request: Request) -> Response:
    zone = request.query_params.get('timezone', 'Europe/Moscow')
    try:
        tz = pytz.timezone(zone)
    except UnknownTimeZoneError:
        return Response(status=400, data={"timezone": "Unknown timezone"})
    moscow_time_now = datetime.now(tz)
    return Response(data={"datetime": moscow_time_now.isoformat(), 'timezone': zone})
