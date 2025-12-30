"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include, re_path

# ...

from config.views import serve_react

urlpatterns = [
    path('api/health/', health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # Catch-all for React SPA (must be last)
    re_path(r'^.*$', serve_react),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

