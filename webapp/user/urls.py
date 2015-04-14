from django.conf.urls import url
from . import views

urlpatterns = [
    url('^authenticate/', views.LoginOrRegisterUserView.as_view(), name='authenticate_user'),
    url('^logout/', views.LogoutUserView.as_view(), name='logout_user'),
]
