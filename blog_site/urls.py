from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_blog/', include('app_blog.urls'))
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]