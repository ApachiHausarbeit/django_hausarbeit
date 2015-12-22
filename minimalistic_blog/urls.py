from django.conf.urls import patterns, url
from minimalistic_blog import views

urlpatterns = patterns('',
    url(r'^$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^article/(?P<id>\d+)/$', views.ArticleTemplateView.as_view(), name='article'),
    url(r'^article/create/$', views.ArticleFormView.as_view(), name='article_create'),
    url(r'^article/(?P<pk>[\w]+)/delete/$', views.ArticleDeleteView.as_view(), name='article_delete'),
    url(r'^article/(?P<pk>[\w]+)/update/$', views.ArticleUpdateView.as_view(), name='article_update'),
    url(r'^article/(?P<id>\d+)/comment/create/$', views.CommentFormView.as_view(), name='comment_create'),
    url(r'^article/(?P<id>\d+)/comment/(?P<pk>[\w]+)/delete/$', views.CommentDeleteView.as_view(), name='comment_delete'),
    url(r'^article/(?P<id>\d+)/comment/(?P<pk>[\w]+)/update/$', views.CommentUpdateView.as_view(), name='comment_update'),
)
