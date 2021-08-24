from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


@cache_page(200)
def main_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'main.html')
