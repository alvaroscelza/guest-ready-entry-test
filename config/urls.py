from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = i18n_patterns(path('', TemplateView.as_view(template_name="index.html")), prefix_default_language=False)
urlpatterns += i18n_patterns(path('admin/', admin.site.urls), prefix_default_language=False)
urlpatterns += i18n_patterns(path('core/', include('applications.core.urls')), prefix_default_language=False)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = settings.APP_NAME
admin.site.index_title = settings.APP_DESCRIPTION
admin.site.site_title = settings.APP_NAME
