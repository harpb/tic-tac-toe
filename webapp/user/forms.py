import re
from django import forms
from django.contrib.auth.models import User, UserManager
from django.contrib.auth import authenticate
from django.utils.translation import ugettext, ugettext_lazy as _

def email_to_username(email_address):
    # Strip up to 30 characters of the prefix before the '@'
    index = email_address.find(u'@')
    username = email_address[:index][:30]

    # Django only allows letters and numbers in username so replace non-alpha numeric characters.
    username = re.sub(r'[^a-zA-Z0-9+]', '', username)

    return username

class AuthenticateForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    email_address = forms.EmailField(max_length = 254)
    password = forms.CharField(label = _("Password"), widget = forms.PasswordInput)
    error_messages = {
        'invalid_login': _("Password does not matches. "
                           "Note that both fields may be case-sensitive."),
        'inactive': _("This account is inactive."),
    }

    def clean_password(self):
        email_address = self.cleaned_data.get('email_address')
        username = email_to_username(email_address)
        password = self.cleaned_data.get('password')

        if username and password:
            try:
                User.objects.get(username = username)
                self.user_cache = authenticate(
                    username = username, password = password)
                if self.user_cache is None:
                    raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code = 'invalid_login',
                    )
            except User.DoesNotExist:
                pass

        return password

    def save(self):
        email_address = self.cleaned_data.get('email_address')
        username = email_to_username(email_address)
        password = self.cleaned_data['password']
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            User.objects.create_user(
                username, email_address, self.cleaned_data['password'])
        finally:
            user = authenticate(username = username, password = password)
        return user
