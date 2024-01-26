"""timesworld_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import LoginPageView, RegistrationPageView, logout, AdminPageView, EditorPageView,StaffPageView, StudentPageView, home
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', LoginPageView.as_view(), name='LoginPage'),
    path('registration', RegistrationPageView.as_view(), name='RegistrationPage'),
    path('home', home, name='home'),
    path('logout', logout, name='logout'),
    path('admin/', AdminPageView.as_view(), name='admin'),
    path('editor/', EditorPageView.as_view(), name='editor'),
    path('staff/', StaffPageView.as_view(), name='staff'),
    path('student/', StudentPageView.as_view(), name='student'),
    path('access-denied/', TemplateView.as_view(template_name="accessdenied.html"), name='access-denied'),
]
