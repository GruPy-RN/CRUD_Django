# -*- coding: utf8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

from models import ItemAgenda
from forms import FormItemAgenda

def lista(request):
	lista_itens = ItemAgenda.objects.all() # Consulta SQL: SELECT * FROM agenda_itemagenda
	return render_to_response("lista.html",
		{'lista_itens': lista_itens})

def adiciona(request):
	form = FormItemAgenda(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			dados = form.cleaned_data # Dicionário que receberá os valores digitados no formulário
			item = ItemAgenda(data=dados['data'], hora=dados['hora'], titulo=dados['titulo'], descricao=dados['descricao'])
			item.save()
			
			return render_to_response("salvo.html", {})

	return render_to_response("adiciona.html", {'form': form}, context_instance=RequestContext(request))

def item(request, nr_item):
	try:
		item = ItemAgenda.objects.get(pk=nr_item) # Buscando o item pela chave primária (pk)
	except ItemAgenda.DoesNotExist:
		raise Http404()
	return render_to_response('item.html', {'item': item})

"""
Opcionalmente, na função item(), pode-se importar 'get_object_or_404' e escrever a função da seguinte forma:

def item(request, nr_item):
	item = get_object_or_404(ItemAgenda, pk=nr_item)
	return render_to_response('item.html', {'item': item})
"""