from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Imovei, Cidade, Visitas


@login_required(login_url='/auth/login')
def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.getlist('tipo')
    cidades = Cidade.objects.all()

    # If para se existir o filtro
    if preco_minimo or preco_maximo or cidade or tipo:
        
        # If's se o formulário do filto estiver vazio
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999
        if not tipo:
            tipo = ['A', 'C']

        # Realiza o filtro    
        imoveis = Imovei.objects.filter(valor__gte=preco_minimo)\
        .filter(valor__lte=preco_maximo)\
        .filter(tipo_imovel__in=tipo).filter(cidade=cidade)
    else:
        # Traz todos os imóveis 
        imoveis = Imovei.objects.all()    
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})

def imovel(request, id):
    # Traz um imóvel existente com tal id ou um erro
    imovel = get_object_or_404(Imovei, id=id)

    # Traz sugestoes de imoveis (mesma cidade, excluindo o id usado)
    sugestoes = Imovei.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]
    return render(request,'imovel.html',{'imovel': imovel, 'sugestoes': sugestoes})

def agendar_visitas(request):
    usuario = request.user
  
    # Dados obtidos pelo método POST enviado pelo formulário no front
    dia = request.POST.get('dia')
    horario = request.POST.get('horario')
    id_imovel = request.POST.get('id_imovel')

    visitas = Visitas(
        imovel_id = id_imovel,
        usuario=usuario,
        dia=dia,
        horario=horario,
    )

    visitas.save()

    return redirect('/agendamentos')

def agendamentos(request):
    # Filtra as visitas do usuário
    visitas=Visitas.objects.filter(usuario=request.user)  

    # Retorna uma página html com as visitas do usuário
    return render(request, 'agendamentos.html', {'visitas': visitas})

def cancelar_agendamento(request, id):
    visitas = get_object_or_404(Visitas, id=id)
    visitas.status = "C"
    visitas.save()
    return redirect('/agendamentos')
