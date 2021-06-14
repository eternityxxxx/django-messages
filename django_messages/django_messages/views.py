from django.contrib import messages
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):

    def get_success_url(self):
        messages.success(self.request, f'Hello, {self.request.user.username}')
        return super(CustomLoginView, self).get_success_url()
