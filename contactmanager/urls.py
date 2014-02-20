from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'', include('social_auth.urls')),
	url(r'^$', 'contact.views.landing', name='landing'),
	url(r'^register/$', 'contact.views.register', name='register'),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'contact.views.logout_page', name='logout_page'),
	url(r'^contacts/$', 'contact.views.contacts', name='contacts'),
	url(r'^contacts/add/$', 'contact.views.add_contact', name='add_contact'),
	url(r'^contacts/(?P<contact_id>.+)/update/$', 'contact.views.update_contact', name='update_contact'),
	url(r'^contacts/(?P<contact_id>.+)/$', 'contact.views.contact_details', name='contact_details'),
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()