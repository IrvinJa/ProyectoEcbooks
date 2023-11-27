from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.views import serve as serve_static
from django.views.static import serve

def _static_butler(request, path, **kwargs):
    return serve_static(request, path, insecure=True, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuarios.urls')),
    path('producto/',include('producto.urls')),
    path('carrito/',include('carrito.urls')),
    path('balance/',include('balance.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),