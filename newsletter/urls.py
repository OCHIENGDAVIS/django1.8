from django.conf.urls import url, include
from .views import contact, about

urlpatterns = [
    url(r"^$", contact, name="contact"),
    url(r"^about/$", about, name="about")
]