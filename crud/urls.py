from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'agenda.views.lista'),
    url(r'^adiciona/$', 'agenda.views.adiciona', name='adiciona'),
    url(r'^item/(?P<nr_item>\d+)/$', 'agenda.views.item'),
)
