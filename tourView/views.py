from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import *


def tour(requst, pk):
    departs = ''
    desc = ''
    titles = ''
    price = ''
    pict = ''

    topinf = ''
    for k, v in departures.items():
        departs += (f'''<li class="nav-item active"> <a class="nav-link" href="/{k}/" data-test="navlink">{v}</a></li>''')

    for i in tours.keys():
        if i == pk:
            desc = tours[pk]["description"]
            titles = tours[pk]["title"] + ' ' + tours[pk]["stars"]+ ' ' +'★'
            price = tours[pk]["price"]

            pict = tours[pk]["picture"]


            topinf = f'''<p class="lead" data-test="lead"><span data-test="country">{tours[pk]["country"]} </span><span data-text="departure">{departures[tours[pk]["departure"]]}</span> <span data-text="nights">{tours[pk]["nights"]}</span> ночей</p>'''

    context = {
        'departs': departs,
        'desc': desc,
        'titles': titles,
        'topinf': topinf,
        'price': price,

        'pict': pict,

    }

    return render(requst, 'tourView/tourpage.html', context)