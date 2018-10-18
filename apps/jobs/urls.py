from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^jobs$', views.jobs_list),
    url(r'^search/$', views.search),
    url(r'^add-job$', views.add_job),
    url(r'^process_job$', views.process_job),
]