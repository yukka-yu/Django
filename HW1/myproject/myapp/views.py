import logging
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

LOGGER = logging.getLogger(__name__)

def log(view):
    def wrapper(request):
        res = view(request)
        LOGGER.info(f'Myapp {view.__name__} page accessed')
        return res
    return wrapper

@log
def index(request):
    template = 'myapp/main_page.html'
    #LOGGER.info('Myapp main page accessed')
    return render(request, template)

@log
def about_me(request):
    template = 'myapp/about_me.html'
    #LOGGER.info('Myapp about me page accessed')
    return render(request, template)

