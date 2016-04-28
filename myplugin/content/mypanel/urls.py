from django.conf.urls import url

from myplugin.content.mypanel import views

urlpatterns = [
    url(r'^nitesh/', views.IndexView.as_view(), name='index'),
]
