from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('maratona_intercon2016.core.urls', namespace='core')),
    url(r'^admin/', admin.site.urls),
]
