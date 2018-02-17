from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

# API URLs
from clients import views as ClientViews
from entries import views as EntryViews

admin.autodiscover()

urlpatterns = [

    # client registration
    url(r'^api/v1/register/$',
        ClientViews.RegisterView.as_view(),
        name='register'),

    # client login
    url(r'^api/v1/login/$',
        ClientViews.LoginView.as_view(),
        name='login'),

    # client profile
    url(r'^api/v1/profile/$',
        ClientViews.ProfileView.as_view(),
        name='profile'),

    # client update password
    url(r'^api/v1/update_password/$',
        ClientViews.UpdatePasswordView.as_view(),
        name='profile'),

    # client new entry
    url(r'^api/v1/new_entry/$',
        EntryViews.NewEntryView.as_view(),
        name='new-entry'),

    # update a entry by id
    url(r'^api/v1/entry/(?P<id>\d+)/$',
        EntryViews.UpdateEntryView.as_view(),
        name='entries-year'),

    # client entries (all)
    url(r'^api/v1/entries/$',
        EntryViews.ListEntriesView.as_view(),
        name='entries-year'),

    # client entries by year
    url(r'^api/v1/entries/(?P<year>\d+)/$',
        EntryViews.ListEntriesView.as_view(),
        name='entries-year'),

    # client entries by month
    url(r'^api/v1/entries/(?P<year>\d+)/(?P<month>\d+)/$',
        EntryViews.ListEntriesView.as_view(),
        name='entries-year'),

    # client entries by year
    url(r'^api/v1/entries/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
        EntryViews.ListEntriesView.as_view(),
        name='entries-year'),

    # admin urls
    url(r'^admin/', include(admin.site.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
