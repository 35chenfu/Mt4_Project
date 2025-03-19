
from django.urls import re_path, include
from django.contrib import admin
import Mt4App.urls

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include(Mt4App.urls)),
]
