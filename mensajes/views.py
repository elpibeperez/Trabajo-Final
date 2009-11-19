from django.template import Context, loader
from django.http import HttpResponse
from sistema.mensajes.models import Mensaje, Sistema_Mensaje
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(redirect_field_name='/')
def index(request):
    t = loader.get_template('index.html')
    mens = Sistema_Mensaje.objects.filter(destino=request.user)
    mensajes = list()
    #TODO Acordate de filtrar por usuarios despues
    for x in mens:
        l = ""
        if (x.mensaje.leido == "T"):
            l = "leido"
        else:
            l = "no leido"
        mensajes.append([l, x.mensaje.rte, x.mensaje.mens[:50],x.mensaje.id])
    html = t.render(Context({
        'mensajes':mensajes,
        'usuario':request.user,
    }))
    return HttpResponse(html)


@login_required(redirect_field_name='/')
def crear(request):
    t = loader.get_template('crear.html')
    html = t.render(Context({}))
    return HttpResponse(html)


@login_required(redirect_field_name='/')
def nuevo_mensaje(request):
    destino = request.POST["para"]
    mns = request.POST["mensaje"]
    users = None
    t = None
    html = None
    try:
         users = User.objects.get(username = destino)
    except  Exception , e:
        pass

    if (users == None): #No existe el destinatario
        t = loader.get_template('crear.html')
        html = t.render(Context({'errores_destinatarios':\
                        "El destinatario no existe","para":destino,\
                        "mens": mns,}))
    elif (mns == ""):
        t = loader.get_template('crear.html')
        html = t.render(Context({'errores_mensaje': \
                        "El mensaje no puede ser vacio","para":destino,}))
    else:
        m = Mensaje(rte=request.user,mens=mns,leido='F')
        m.save()
        s = Sistema_Mensaje(mensaje = m,destino = users)
        s.save()
        t = loader.get_template('exito.html')
        html = t.render(Context({}))
    return HttpResponse(html)


@login_required(redirect_field_name='/')
def leer(request, mensaje_id):
    mensaje = Mensaje.objects.get(pk=mensaje_id)
    t = loader.get_template('leer.html')
    if(mensaje.leido=="F"):
        mensaje.leido = "T"
        mensaje.save()
    html = t.render(Context({"de":mensaje.rte ,"mens":mensaje.mens,"id":mensaje_id, }))
    return HttpResponse(html)


@login_required(redirect_field_name='/')
def responder(request):
    mens = Mensaje.objects.get(pk=request.POST["id"])
    t = loader.get_template('crear.html')
    html = t.render(Context({"para":mens.rte, "mens":mens.mens}))
    return HttpResponse(html)

    
@login_required(redirect_field_name='/')
def borrar(request):
    id = None
    try:
        mns = Mensaje.objects.get(pk=request.POST["id"])        
        sist = Sistema_Mensaje.objects.get(mensaje=mns, destino= request.user)
        sist.delete()
        if len(Sistema_Mensaje.objects.filter(mensaje = mns)) == 0:
            mns.delete()
        t = loader.get_template('borrar.html')
        html = t.render(Context({'mensaje':'Se borro con exito el mensaje'}))
        return HttpResponse(html)
    except  Exception, e:
        t = loader.get_template('borrar.html')
        html = t.render(Context({'mensaje':'Hubo problemas con los Ids'}))
        return HttpResponse(html)
    pass
        
    
    
