from django.template import Context, loader
from django.http import HttpResponse
from sistema.grupos.models import Usuarios, Grupo 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


@login_required(redirect_field_name='/')
def index(request):
    t = loader.get_template('grupos_home.html')
    gids = Usuarios.objects.filter(usuario=request.user)
    grs = list()
    for x in gids:
        if(x.rol == "P"):
            grs.append([x.grupo.tema,"publicador",x.grupo.id])
        else:
            grs.append([x.grupo.tema,"colaborador",x.grupo.id])
    html = t.render(Context({
        'grupos':grs,
        'usuario':request.user,
    }))
    return HttpResponse(html)

@login_required(redirect_field_name='/')
def argentina(request):
    t = loader.get_template('grupos_argentina.html')
    html = t.render(Context({}))
    return HttpResponse(html)
    
