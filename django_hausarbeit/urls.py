from django.conf.urls import include, url
from django.contrib import admin
from minimalistic_blog.auth import logout_view, register
from django_hausarbeit import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index.IndexView.as_view(), name='index'),
    url(r'^blog/', include('minimalistic_blog.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^accounts/logout/$', logout_view, name='logout'),
    url(r'^accounts/register/$', register, name='register'),
]
