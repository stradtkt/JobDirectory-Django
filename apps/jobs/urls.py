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
    url(r'^add-profile$', views.add_profile),
    url(r'^add-past-jobs$', views.add_past_jobs),
    url(r'^process_past_jobs$', views.process_past_jobs),
    url(r'^jobs/(?P<id>\d+)$', views.job_single),
    url(r'^jobs/(?P<id>\d+)/apply-for-job$', views.apply_for_job),
]