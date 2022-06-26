from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('note.urls')),
    path('', RedirectView.as_view(url='notes/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('tinymce/', include('tinymce.urls')),
]+ (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
