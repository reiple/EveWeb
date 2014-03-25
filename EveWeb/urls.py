from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EveWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^test/$', 'Board.views.ViewBoardList'),
    url(r'^login/$', 'Login.views.LoginTest'),
    url(r'^member/$', 'Login.views.GetMemberList'),
    url(r'^wormhole/$', 'Login.views.GetWormholeMemberList'),
)
