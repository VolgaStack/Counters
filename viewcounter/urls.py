from django.conf.urls import url

from viewcounter.views import ViewsCounterMain, ViewsCounterGet

urlpatterns = [
	url(r'^$',ViewsCounterMain.as_view()),
    url(r'^get/',ViewsCounterGet.as_view()),
    ]
