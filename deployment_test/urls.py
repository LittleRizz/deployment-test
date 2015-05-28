from django.conf.urls import include, url
from django.contrib import admin
from blogtime.views import homeview

urlpatterns = [
    # Examples:
    # url(r'^$', 'deployment_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'blogtime.views.homeview', name='home'),
]
