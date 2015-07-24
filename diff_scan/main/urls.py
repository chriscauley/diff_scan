from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
  '',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^test/(\d+)/','main.views.test'),
  url(r'^bulk_add_url/','main.views.bulk_add_url'),
)

if settings.DEBUG:
  urlpatterns += patterns(
    '',
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,
         'show_indexes': True}),
    )
