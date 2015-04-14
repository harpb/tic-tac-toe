from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
import user

urlpatterns = [
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    url(r'^tic_tac_toe/', include('tic_tac_toe.urls')),
    url(
        r'^todo/$',
        TemplateView.as_view(template_name = 'todo_index.html'),
        name = 'todo_index'),

    url(r'^admin/', include(admin.site.urls)),
    url('^user/', include('user.urls'))
]
