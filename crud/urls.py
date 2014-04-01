# -*- coding: utf8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), # Para a criação de painel de administração. Não será usado neste exemplo
    url(r'^$', 'agenda.views.lista'), # Exibe os itens listados
    url(r'^adiciona/$', 'agenda.views.adiciona', name='adiciona'), # Formulário do template "adiciona.html"
    url(r'^item/(?P<nr_item>\d+)/$', 'agenda.views.item'), # URL individual para cada item cadastrado
)
