from django.conf.urls import patterns, include, url
from main.views import main, graph
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fbnetworkgraph.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^main/$', main),
    (r'^graph', graph),

    url(r'^admin/', include(admin.site.urls)),
)
