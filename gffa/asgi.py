"""
ASGI config for gffa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
>>>>>>> 9f3b8368c63a623cee5f5551eaa906c500ed1e5f
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gffa.settings')

application = get_asgi_application()
