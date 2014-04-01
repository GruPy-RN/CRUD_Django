# -*- coding: utf8 -*-

from django import forms
from django.forms import ModelForm
from agenda.models import ItemAgenda

class ItemAgendaForm(ModelForm):
	data = forms.DateField(
		widget = forms.DateInput(format='%d/%m/%Y'),
		input_formats=['%d/%m/%y', '%d/%m/%Y'])

	class Meta:
		model = ItemAgenda
		fields = ('titulo', 'data', 'hora', 'descricao')

"""
class FormItemAgenda(forms.Form):
	data = forms.DateField(
		widget = forms.DateInput(format='%d/%m/%Y'),
		input_formats=['%d/%m/%y', '%d/%m/%Y']
	)
	hora = forms.TimeField()
	titulo = forms.CharField(max_length = 100)
	descricao = forms.CharField()
"""