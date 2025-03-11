from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('counter.urls'))
]

#user valerienev password valeri12345 