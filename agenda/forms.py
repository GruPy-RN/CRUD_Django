# -*- coding: utf8 -*-

from django import forms
from models import ItemAgenda

class FormItemAgenda(forms.Form):
	data = forms.DateField(
		widget = forms.DateInput(format='%d/%m/%Y'),
		input_formats=['%d/%m/%y', '%d/%m/%Y']
	)
	hora = forms.TimeField()
	titulo = forms.CharField(max_length = 100)
	descricao = forms.CharField()