# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if request.session.get('your_gold') is None:    
        request.session['your_gold'] = 0
    if request.session.get('action') is None:
        request.session['action'] = ''

    context = {
        'gold' : request.session['your_gold'],
        'activity' : request.session['action']
    }
    
    print 'made it to index'
    print request.session['your_gold']
    return render(request, 'index.html', context)

def process(request, path):
    if path == 'farm':
        print "went to farm"
        farm_gold = random.randint(10,21)
        request.session['your_gold'] += farm_gold
        request.session['action'] = "You found {} gold at the farm.".format(farm_gold)
        return redirect('/')
    if path == 'cave':
        print 'went to cave'
        cave_gold = random.randint(5,11)
        request.session['your_gold'] += cave_gold
        request.session['action'] = "You found {} gold in the cave.".format(cave_gold)
        return redirect('/')
    if path == 'house':
        print 'went to house'
        house_gold = random.randint(2,6)
        request.session['your_gold'] += house_gold
        request.session['action'] = "You found {} gold in the house.".format(house_gold)
        return redirect('/')
    if path == 'casino':
        if request.session['your_gold'] > 0:
            casino_gold = random.randint(-50, 51)
            request.session['your_gold'] += casino_gold
            if casino_gold < 0:
                request.session['action'] = 'You lost {} gold at the casino.'.format(casino_gold)
            else:
                request.session['action'] = 'You won {} gold at the casino.'.format(casino_gold)
            print 'went to casino'
            return redirect('/')
        elif request.session['your_gold'] <= 0:
            request.session['action'] = "You can't go to the casino. You have no money."
            return redirect('/')
def reset(request): 
    request.session['your_gold'] = 0
    request.session['action'] = ''
    return redirect('/')
        
# Create your views here.