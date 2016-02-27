# instablog/urls.py
from django.conf.urls import url
from django.contrib import admin

from blog.views import hello
from blog.views import hello_with_template


urlpatterns = [
    url(r'^$', hello),
    url(r'^hello/$', hello_with_template),
    url(r'^admin/', admin.site.urls),
]

