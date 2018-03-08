from django.conf.urls import url

from .views import LeadsList

urlpatterns = [
    url(r'^$', LeadsList.as_view(), name='leads-list'),
]
