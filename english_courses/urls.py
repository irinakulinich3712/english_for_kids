from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('english-courses-management/', admin.site.urls),
    path('', include('main.urls'))
]
