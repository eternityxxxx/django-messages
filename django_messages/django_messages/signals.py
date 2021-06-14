from django.contrib import messages
from django.contrib.auth import user_logged_in
from django.dispatch import receiver


@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    print('HEY')
    messages.info(request, "Welcome ...")
