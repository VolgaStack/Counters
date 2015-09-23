from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('viewcounter.urls', namespace="viewcounter-app")),
    url(r'^admin/', include(admin.site.urls)),
    ]
