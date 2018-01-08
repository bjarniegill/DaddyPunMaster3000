from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from daddypunmaster3000.views import AddJoke, Choose, Jokes, PickSession, ResetSessions
from daddypunmaster3000.api import CommitToJoke, CreateSession, RetrieveRandomJoke


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', PickSession.as_view()),
    url(r'^add/$', AddJoke.as_view()),
    url(r'^([a-z0-9]{4})/group/(\d+)/', Jokes.as_view()),
    url(r'^([a-z0-9]{4})$', Choose.as_view(), name='choose'),
    url(r'reset/$', ResetSessions.as_view()),

    url(r'^api/joke/(\d+)/([a-z0-9]{4})$', RetrieveRandomJoke.as_view()),
    url(r'^api/commit/$', CommitToJoke.as_view()),
    url(r'^api/create/$', CreateSession.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
