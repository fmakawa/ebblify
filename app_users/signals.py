from django.dispatch import Signal

# Sent when a  User signed up
user_sign_up = Signal(providing_args=['user'])
