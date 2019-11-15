"""sensoroad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include  # This needs to be added
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views
from sensoroad.apps.api import urls as api_urls
from sensoroad.apps.user.forms import UserLoginForm
from sensoroad.apps.dashboard.views import dashboard_view
from sensoroad.apps.user.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('^api/', include(api_urls)),

    url('^$', dashboard_view, name='dashboard'),
    url('^dashboard/$', dashboard_view, name='dashboard'),
    url('^login/$', views.LoginView.as_view(
        template_name="login.html",
        authentication_form=UserLoginForm),
        name='login'
        ),
    url('^register/$', SignUpView.as_view(),
        name='register'
        ),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
