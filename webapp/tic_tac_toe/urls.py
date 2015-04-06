from django.conf.urls import url
from . import views

urlpatterns = [
#     url(r'^(?P<board>\w+)/$', views.NextMoveView.as_view(), name='next-move'),
    url(r'^next_move/$', views.NextMoveView.as_view(), name='next-move'),
]
