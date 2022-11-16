from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Tecnologias, Nicho_mercado, Empresa
from django.contrib import messages
from django.contrib.messages import constants
from django.db import models
from django.forms import ModelForm
import re
import time as t

# Create your views here.


def nova_empresa(request):
    if request.method == "GET":
        nichos = Nicho_mercado.objects.all()
        techs = Tecnologias.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs, 'nichos': nichos})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteristicas = request.POST.get('caracteristicas')
        tecnologias = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')

    # Variável local que armazena todos os
    # nichos disponíveis para iterar e validar
    it_nicho = list(Nicho_mercado.objects.values())

    result = re.findall(r'^\w*', nicho)
    pattern = re.findall(r'^\d*', nicho)
    compare = pattern == result

    print(f"Aqui pô: {result}\n"+f"Pattern: {pattern}"+f"\nÉ igual? {compare}")

    if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or len(nicho.strip()) == 0 or len(caracteristicas.strip()) == 0 or (not logo)):
        messages.add_message(request, constants.ERROR,
                             'Preencha todos os campos')
        return redirect('/home/nova_empresa')

    if logo.size > 100_000_000:
        messages.add_message(request, constants.ERROR,
                             'Logo da empresa deve ter menos de 10MB')
        return redirect('/home/nova_empresa')

    if nicho not in [i['id'] for i in it_nicho]:
        messages.add_message(request, constants.ERROR,
                             'Nicho de mercado: "'+nicho+'" inválido')
        return redirect('/home/nova_empresa', kwargs="nome, email, cidade")

    empresa = Empresa(logo=logo,
                      nome=nome,
                      email=email,
                      cidade=cidade,
                      nicho_mercado_id=nicho,
                      endereco=endereco,
                      caracteristica_empresa=caracteristicas)
    empresa.save()
    empresa.tecnologias.add(*tecnologias)
    empresa.save()
    messages.add_message(request, constants.SUCCESS,
                         'Empresa cadastrada com sucesso')
    return redirect('/home/empresas')


def empresas(request):
    technologias_filtrar = request.GET.get('tecnologias')
    nome_filtrar = request.GET.get('nome')
    empresas = Empresa.objects.all()

    if technologias_filtrar:
        empresas = empresas.filter(tecnologias=technologias_filtrar)

    if nome_filtrar:
        empresas = empresas.filter(nome__icontains=nome_filtrar)

    tecnologias = Tecnologias.objects.all()
    return render(request, 'empresa.html', {'empresas': empresas, 'tecnologias': tecnologias})


def excluir_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.add_message(request, constants.SUCCESS,
                         'Empresa deletada com sucesso')
    return redirect('/home/empresas')


def empresa(request, id):
    empresa_unica = get_object_or_404(Empresa, id=id)
    return render(request, 'empresa_unica.html', {'empresa': empresa_unica})


def home_redirect(request):
    tempo = {'t': 10, }
    current_time = t.localtime()
    timestamp = t.strftime("%I:%m", current_time)
    text = f'Você será redirecionado em instantes\n' + \
        f'- Current Time: {timestamp}'
    messages.add_message(request, constants.INFO, text)
    return render(request, 'redirect.html', tempo)
