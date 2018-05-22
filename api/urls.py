from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

# API URLs
from app import views as AppViews
from clients import views as ClientViews
from entries import views as EntryViews

admin.autodiscover()

urlpatterns = [

    # admin urls
    url(r'^admin/', include(admin.site.urls)),

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
        name='update_password'),

    # client update profile
    url(r'^api/v1/update_profile/$',
        ClientViews.UpdateProfileiew.as_view(),
        name='update_funds'),

    # client new entry
    url(r'^api/v1/new_entry/$',
        EntryViews.NewEntryView.as_view(),
        name='new_entry'),

    # client new recurrent entry
    url(r'^api/v1/new_recurrent/$',
        EntryViews.NewRecurrentEntryView.as_view(),
        name='new_recurrent'),

    # update a entry by id
    url(r'^api/v1/entry/(?P<id>\d+)/$',
        EntryViews.UpdateEntryView.as_view(),
        name='update_entry'),

    # update a recurrent entry by id
    url(r'^api/v1/recurrent_entry/(?P<id>\d+)/$',
        EntryViews.UpdateRecurrentEntryView.as_view(),
        name='update_recurrent_entry'),

    # delete a entry by id
    url(r'^api/v1/entry/(?P<id>\d+)/delete/$',
        EntryViews.DeleteEntryView.as_view(),
        name='delete_entry'),

    # delete a recurrent entry by id
    url(r'^api/v1/recurrent_entry/(?P<id>\d+)/delete/$',
        EntryViews.DeleteRecurrentEntryView.as_view(),
        name='delete_recurrent_entry'),

    # client entries (all)
    url(r'^api/v1/entries/$',
        EntryViews.ListEntriesView.as_view(),
        name='all_entries'),

    # client entries (all)
    url(r'^api/v1/recurrent_entries/$',
        EntryViews.ListRecurrentEntriesView.as_view(),
        name='all_recurrent_entries'),

    # client entries by year
    url(r'^api/v1/entries/(?P<year>\d+)/$',
        EntryViews.ListEntriesView.as_view(),
        name='entries_year'),

    # client entries by month
    url(r'^api/v1/entries/(?P<year>\d+)/(?P<month>\d+)/$',
        EntryViews.ListEntriesView.as_view(),
        name='entries_month'),

    # client entries by year
    url(r'^api/v1/entries/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
        EntryViews.ListEntriesView.as_view(),
        name='entries_day'),

    # client index
    url(r'^', AppViews.index, name='index')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
