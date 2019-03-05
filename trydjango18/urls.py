from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# app_name = "newsletter"

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^accounts/', include('registration.backends.default.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
