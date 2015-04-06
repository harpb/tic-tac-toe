from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    url(r'^tic_tac_toe/', include('tic_tac_toe.urls')),

#     url(r'^admin/', include(admin.site.urls)),
]
