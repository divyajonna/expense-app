from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
# from django.conf.urls.static import static
admin.site.site_header = 'Expense Super Admin' # this will change django admin title

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
]

if settings.ADMIN_ENABLED:
    urlpatterns.append(url(r'^admin/', admin.site.urls))