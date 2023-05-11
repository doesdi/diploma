from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from Management import settings
from .views import *

urlpatterns = [
    path('', tasks),
    path('admin/', admin.site.urls),
    path('', include('modules.blog.urls')),
    path('', include('modules.system.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns

