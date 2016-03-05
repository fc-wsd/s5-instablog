# instablog/urls.py
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from django.conf import settings

from blog import views as blog_views


urlpatterns = [
    url(r'^posts/create/$', blog_views.create_post, name='create_post'),
    url(r'^$', blog_views.list_posts),
    url(
        r'^posts/(?P<pk>[0-9]+)/$', blog_views.view_post, name='view_post'
    ),
    url(r'^hello/$', blog_views.hello_with_template),
    url(r'^admin/', admin.site.urls),
    url(
        r'^{}$'.format(settings.LOGIN_URL[1:]),  # r'^login/$'
        django_login,
        {'template_name': 'login.html'},
        name='login_url',
    ),
    url(
        r'^{}$'.format(settings.LOGOUT_URL[1:]),  # r'^logout/$'
        django_logout,
        {'next_page': settings.LOGIN_URL},
        name='logout_url',
    ),
]

