# -*- coding: utf8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import ItemAgenda
from forms import FormItemAgenda

def lista(request):
	lista_itens = ItemAgenda.objects.all() # SELECT * FROM agenda_itemagenda
	return render_to_response("lista.html",
		{'lista_itens': lista_itens})

def adiciona(request):
	form = FormItemAgenda(request.POST or None, request.FILES or None)
	
	if request.method == 'POST':
		if form.is_valid():
			dados = form.cleaned_data
			item = ItemAgenda(data=dados['data'], hora=dados['hora'], titulo=dados['titulo'], descricao=dados['descricao'])
			item.save()
			
			return render_to_response("salvo.html", {})

	return render_to_response("adiciona.html", {'form': form}, context_instance=RequestContext(request))
