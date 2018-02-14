from authentication import views as auth_views
from callback import views as callback_views
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from djoser import urls
from djoser import views as djoser_views
from djoser.urls import authtoken
from extract import views as extract_views
from oauth import views as oauth_views
from plans import views as plan_views
from rentability import views as rentability_views
from sales import views as sales_views
from simulator import views as simulator_views
from swagger import views as swagger_views

from rest_framework_expiring_authtoken import views

admin.autodiscover()

urlpatterns = [

    # url(r'^v1/auth/exploit/',
    #     auth_views.CustomExploitView.as_view(),
    #     name='exploit'),

    # admin urls
    url(r'^admin/', include(admin.site.urls))
]
