from django.conf.urls import url
from django.contrib import admin

from triinjalauri.views import home, where, gallery, transport, faq

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^oko/$', where, name='where'),
    url(r'^galerii/$', gallery, name='gallery'),
    url(r'^transport/$', transport, name='transport'),
    url(r'^kkk/$', faq, name='faq'),
    url(r'^admin/', admin.site.urls),
]
