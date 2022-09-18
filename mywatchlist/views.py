from django.shortcuts import render
from mywatchlist.models import MyWatchlistItem
from django.http import HttpResponse
from django.core import serializers
# TODO: Create your views here.

def show_mywatchlist(request):
    context = {
    'nama': 'Yudi Putra Sabri',
    'npm': 2106706123,
    }
    return render(request, "main.html", context)

data = MyWatchlistItem.objects.all()

context = {
    'list_movie': data,
    'nama': 'Yudi Putra Sabri',
    'npm': 2106706123,
}

def show_mywatchlist_html(request):
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_mywatchlist_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")