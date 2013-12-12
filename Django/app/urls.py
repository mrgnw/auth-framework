from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views



#4 PHOTOHELP skipping to 5 because 4 is handling an upload with Django (we're using AngularJS)
#5 PHOTOHELP
from django.conf.urls.static import static
from project import settings

#  Added "+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)" to end
urlpatterns = patterns('app.views', url(r'^addresses$', views.AddressList.as_view(), name='address-list'),
                       url(r'^addresses/(?P<pk>[0-9]+)$', views.AddressDetail.as_view(), name='address-detail'),
                       url(r'^users$', views.UserList.as_view(), name='user-list'),
                       url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='user-detail'),
                       url(r'^recipes$', views.RecipeList.as_view(), name='recipe-list'),
                       url(r'^recipes/(?P<pk>[0-9]+)$', views.RecipeDetail.as_view(), name='recipe-detail'),
                       url(r'^tags/(?P<pk>[0-9]+)$', views.TagDetail.as_view(), name='tag-detail'),
                       url(r'^tags$', views.TagList.as_view(), name='tag-detail'),
                       url(r'^recipe-lists$', views.RecipeListList.as_view(), name='recipe-list-list'),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
)

urlpatterns = format_suffix_patterns(urlpatterns)
