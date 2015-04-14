# Create your views here.
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from .forms import AuthenticateForm
from django.contrib.auth import login, logout
from django.views.generic.base import View, RedirectView

class LoginOrRegisterUserView(FormView):
    form_class = AuthenticateForm
    template_name = 'authenticate_user.html'
    success_url = reverse_lazy('tic_tac_toe_index')

    def form_valid(self, form):
        """
        If the form is valid, save the model and login the user
        """
        user = form.save()
        login(self.request, user)
        return super(LoginOrRegisterUserView, self).form_valid(form)

class LogoutUserView(RedirectView):

    url = reverse_lazy('tic_tac_toe_index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutUserView, self).get(request, *args, **kwargs)
