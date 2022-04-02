"""gffa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
=======
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
>>>>>>> 9f3b8368c63a623cee5f5551eaa906c500ed1e5f
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
=======

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', lambda r: HttpResponseRedirect('apps/webapp/')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('apps/webapp/', include('apps.webapp.urls')),
    path('api/', include('apps.api.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 9f3b8368c63a623cee5f5551eaa906c500ed1e5f
