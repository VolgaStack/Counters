from django.conf.urls import url

from viewcounter.views import ViewsCounterMain, ViewsCounterGet

urlpatterns = [
	url(r'^ASKYA',ViewsCounterMain.as_view()),
    url(r'^GET',ViewsCounterGet.as_view()),
    ]
