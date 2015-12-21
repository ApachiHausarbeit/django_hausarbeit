from django.conf.urls import patterns, url
from minimalistic_blog import views

urlpatterns = patterns('',
    url(r'^article-list/$', views.ArticleListView.as_view(), name = 'article_list'),
    url(r'^article-create/$', views.ArticleFormView.as_view(), name = 'article_create'),
    url(r'^article-show/(?P<blog_id>\d+)/$', views.ArticleTemplateView.as_view(), name = 'article_show'),
    url(r'^article-delete/(?P<pk>[\w]+)/$', views.ArticleDeleteView.as_view(), name = 'article_delete'),
    url(r'^comment-create/$', views.CommentFormView.as_view(), name = 'comment_create'),
    url(r'^comment-delete/$', views.CommentDeleteView.as_view(), name = 'comment_create'),
)
    
