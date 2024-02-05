from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)

def games(request):
    logger.info('Main GamePage Accessed')
    return HttpResponse('GAMES!!!')

def head_tail(request):
    mess = ['head', 'tail']
    res = mess[randint(0, 1)]
    logger.info(f'Head_tail Page accessed with result {res}')
    return HttpResponse(res)

def dice(request):
    res = randint(1, 6)
    logger.info(f'Dice page accessed with result {res}')
    return HttpResponse(res)

def rand(request):
    res = randint(0, 100)
    logger.info(f'Rand page accessed with result {res}')
    return HttpResponse(res)

