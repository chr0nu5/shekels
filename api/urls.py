from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

    # url(r'^v1/auth/exploit/',
    #     auth_views.CustomExploitView.as_view(),
    #     name='exploit'),

    # admin urls
    url(r'^admin/', include(admin.site.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
