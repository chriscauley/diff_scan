from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
  '',
  url(r'^$', 'main.views.index'),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^page/(\d+)/','main.views.page_detail',name="page_detail"),
  url(r'^bulk_add_url/','main.views.bulk_add_url'),
  url(r'^page/(clear|test)/(\d+)/$','main.views.action',name="page_action"),
  url(r'^page/(clear|test)/(\d+)/(\d+)/$','main.views.action',name="page_action"),
  url(r'^media_files/',include('media.urls')),
)

if settings.DEBUG:
  urlpatterns += patterns(
    '',
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,
         'show_indexes': True}),
    )
