from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .settings import BUS_STATION_CSV
import csv

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    all_stations = []
    with open(BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_stations.append(row)

    paginator = Paginator(all_stations, 20)
    current_page = request.GET.get('page', 1)
    stations = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if stations.has_previous():
        prev_page = stations.previous_page_number
    if stations.has_next():
        next_page = stations.next_page_number

    return render_to_response('index.html', context={
        'bus_stations': stations,
        'current_page': stations.number,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })

