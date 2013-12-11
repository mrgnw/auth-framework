from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('backend.views',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('app.urls'))
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
