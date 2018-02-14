from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from oauth import views as oauth_views

admin.autodiscover()

urlpatterns = [

    # url(r'^v1/auth/exploit/',
    #     auth_views.CustomExploitView.as_view(),
    #     name='exploit'),

    # admin urls
    url(r'^admin/', include(admin.site.urls))
]
