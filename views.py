from django.template import Context, loader
from django.http import HttpResponse
from django.contrib import auth
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    t = loader.get_template('login.html')
    html = t.render(Context({}))
    return HttpResponse(html)


def login(request):
    login = request.POST["nombre"]
    pas = request.POST["pass"]
    html = None
    #el menu de opciones de html
    user = auth.authenticate(username=login, password=pas)
    if user is not None:
        #lo debo loguear
        t = get_template('home.html')
        auth.login(request,user)
        html = t.render(Context({"usuario":user}))
    else:
        t = get_template('log_error.html')
        html = t.render(Context({}))
    return HttpResponse(html)


@login_required(redirect_field_name='/')
def desloguear(request):
    logout(request)
    t = loader.get_template('login.html')
    html = t.render(Context({}))
    return HttpResponse(html)


