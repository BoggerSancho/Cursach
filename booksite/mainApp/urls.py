from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='index'),
    # url(r'^news/$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
    #                                   template_name="news/posts.html")),
    # url(r'^news/(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name="news/post.html"))
]