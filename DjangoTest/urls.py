from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from mysite.views import hello, current_datetime

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
)
