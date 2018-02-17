from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

# API URLs
from clients import views as ClientViews

admin.autodiscover()

urlpatterns = [

    url(r'^api/v1/register/',
        ClientViews.RegisterView.as_view(),
        name='register'),

    url(r'^api/v1/login/',
        ClientViews.LoginView.as_view(),
        name='login'),

    url(r'^api/v1/profile/',
        ClientViews.ProfileView.as_view(),
        name='profile'),

    url(r'^api/v1/update_password/',
        ClientViews.UpdatePasswordView.as_view(),
        name='profile'),

    # admin urls
    url(r'^admin/', include(admin.site.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
