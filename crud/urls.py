from django.conf.urls import include, url
from django.views.generic import RedirectView

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^leads/', include(('leads.urls', 'leads'), 'leads')),
    url(r'^$', RedirectView.as_view(pattern_name='leads:leads-list', permanent=False)),
]
