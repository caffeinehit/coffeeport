from django.conf import settings
from django.conf.urls import patterns, include, url

from .app.views import *

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name = 'index'),
    url(r'^burgers/$', BurgerIndexView.as_view(), name = 'burgers'),

    # Heroku static
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
