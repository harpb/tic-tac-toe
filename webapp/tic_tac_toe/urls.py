from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(
        r'^tic_tac_toe_realtime/$',
        TemplateView.as_view(template_name = 'tic_tac_toe_index.html'),
        name = 'tic_tac_toe_index'),
    url(r'^next_move/$', views.NextMoveView.as_view(), name='next-move'),
]
