"""QuestionTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic.base import RedirectView
from core.views import IndexTemplateView
from django_registration.backends.one_step.views import RegistrationView
from users.forms import CustomUserForm
from app import views
from django.conf.urls.static import static
from django.conf import settings
from users import view as user_views
from django.contrib.auth import views as auth_views

# https://django-registration.readthedocs.io/en/3.0/activation-workflow.html

urlpatterns = [
     path('admin/', admin.site.urls),


     path('register/',user_views.register,name='register'),

     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            user_views.activate, name='activate'),
            

     path("accounts/register/",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/",
         ), name="django_registration_register"),

     path("accounts/",
         include("django_registration.backends.one_step.urls")),

     path("accounts/",
         include("django.contrib.auth.urls")),

 
     path("api/",
         include("users.api.urls")),

     path("api/",
         include("app.api.urls")),

     url('^', include('django.contrib.auth.urls')),

     path("api-auth/",
         include("rest_framework.urls")),

     path("api/rest-auth/",
         include("rest_auth.urls")),

     path("api/rest-auth/registration/",
         include("rest_auth.registration.urls")),
 
     path("match/", views.matchplayed, name='matchplayed'),

     url(r'match/(?P<id>[0-9]+)/delete/$', views.deletematch, name='deletematch'),

     path('accounts/', include('allauth.urls')),

    path('repass/',include('password_reset.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
