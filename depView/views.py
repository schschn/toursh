from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import *

def dep(requst, vname):

    departs = ''
    toursdep = ''
    name = ''
    num = 1
    for k, v in departures.items():
        departs += (f'''<li class="nav-item active"> <a class="nav-link" href="/{k}/" data-test="navlink">{v}</a></li>''')

    if vname in deps:
        for i in tours:
            if tours[i]['departure'] == vname:
                name = departures[vname]
                toursdep += f'''<div class="col-4" data-test="card">
            <div class="card mb-3" >
            <img src="{tours[i]['picture']}" class="card-img-top img-fluid" data-test="picture">
            <div class="card-body">
                <h5 class="card-title">{tours[i]['country']}: {tours[i]['title']}</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <h6 class="card-title">{tours[i]['date']}, {tours[i]['nights']} дней, {tours[i]['price']} RUB, {tours[i]['stars']} stars</h6>
                <a href="/tours/{num}" class="btn btn-sm btn-primary" data-test="tourlink">Подробнее</a>
         </div>
        </div>
        </div>'''
            num +=1
    else:
        raise Http404('There is no such direction.')

    context = {
        'name': name,
        'departs': departs,
        'toursdep': toursdep
    }

    return render(requst, 'depView/deppage.html', context)
