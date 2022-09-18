from django.shortcuts import render
from mywatchlist.models import MyWatchlistItem
from django.http import HttpResponse
from django.core import serializers
# TODO: Create your views here.
data = MyWatchlistItem.objects.all()
def show_mywatchlist(request):
    result = ""
    watched = 0
    unwatched = 0

    for a in data:
        if (a.watched_movie): watched += 1
        else: unwatched += 1

    if watched > unwatched : result = "Selamat, kamu sudah banyak menonton!"
    if watched == unwatched : result = "Waduh, Kamu menonton setengah dari list kamu, ayo tambah lagi!"
    else : result = "Wah, kamu masih sedikit menonton!"    

    context = {
    'nama': 'Yudi Putra Sabri',
    'npm': 2106706123,
    'result' :result,
    'watched' : watched,
    'unwatched' : unwatched,
    }

    return render(request, "main.html", context)


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