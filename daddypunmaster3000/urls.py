from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from daddypunmaster3000.views import AddJoke, Choose, Jokes
from daddypunmaster3000.api import CommitToJoke, RetrieveRandomJoke


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^add/$', AddJoke.as_view()),
    url(r'^group/(\d+)/', Jokes.as_view()),
    url(r'^$', Choose.as_view()),

    url(r'^api/joke/(\d+)$', RetrieveRandomJoke.as_view()),
    url(r'^api/commit/$', CommitToJoke.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
