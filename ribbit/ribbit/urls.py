from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
<<<<<<< HEAD
    url(r'^$', 'ribbit_app.views.index'), # root
    url(r'^login$', 'ribbit_app.views.login_view'), # login
    url(r'^logout$', 'ribbit_app.views.logout_view'), # logout
    url(r'^signup$', 'ribbit_app.views.signup'), # signup
    url(r'^submit$','ribbit_app.views.submit'), #submit new ribbit
=======
    url(r'^$', 'ribbit_app.views.index'),
    url(r'^login$', 'ribbit_app.views.login_view'),
    url(r'^logout$', 'ribbit_app.views.logout_view'),
    url(r'^signup$', 'ribbit_app.views.signup'),
    url(r'^ribbits$', 'ribbit_app.views.public'),
    url(r'^submit$', 'ribbit_app.views.submit'),
    url(r'^users/$', 'ribbit_app.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'ribbit_app.views.users'),
    url(r'^follow$', 'ribbit_app.views.follow'),
>>>>>>> 8991acd7d362175709df18365c47d25a648daa44
)
