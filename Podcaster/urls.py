from django.contrib import admin
from django.conf import settings  ##新增
from django.conf.urls import include
from django.urls import re_path as url
from django.contrib import admin
from django.urls import re_path, path
from django.views import static  ##新增
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('', include('article.urls')),
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
]

# handler404 = views.page_not_found
# handler500 = views.server_error
# handler400 = views.bad_request
