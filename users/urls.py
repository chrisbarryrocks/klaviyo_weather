from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^success', views.success, name='success'),
    url(r'', views.signup, name='signup'),
]
