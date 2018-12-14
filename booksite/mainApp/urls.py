from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from .views import List


urlpatterns = [
    url(r'^$', List.as_view(), name='index'),
    url(r'^register$', views.register, name='register'),
    # url(r'^news/$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
    #                                   template_name="news/posts.html")),
    # url(r'^news/(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name="news/post.html"))

]