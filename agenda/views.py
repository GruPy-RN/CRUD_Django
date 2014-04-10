# -*- coding: utf8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from models import ItemAgenda
from forms import ItemAgendaForm

def lista(request):
	lista_itens = ItemAgenda.objects.all() # Consulta SQL: SELECT * FROM agenda_itemagenda
	return render_to_response("lista.html", {'lista_itens': lista_itens})

def adiciona(request):
	if request.method == "POST":
		form = ItemAgendaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('salvo.html', {})
		else:
			form = ItemAgendaForm()
			return render_to_response('item.html', {'form': form}, context_instance=RequestContext(request))

def item(request, nr_item):
	item = get_object_or_404(ItemAgenda, pk=nr_item) # Buscando o item pela chave primária (pk)
	if request.method == "POST":
		form = ItemAgendaForm(request.POST, request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return render_to_response('salvo.html', {})
		else:
			form = ItemAgendaForm(instance=item)
			return render_to_response('item.html', {'form': form}, context_instance=RequestContext(request))

def apaga(request, nr_item):
	item = get_object_or_404(ItemAgenda, pk=nr_item) # Buscando o item pela chave primária (pk)
	if request.method == "POST":
		form = ItemAgendaForm(request.POST, request.FILES, instance=item)
		if form.is_valid():
			form.delete()
			return render_to_response('apagado.html', {})
		else:
			form = ItemAgendaForm(instance=item)
			return render_to_response('item.html', {'form': form}, context_instance=RequestContext(request))