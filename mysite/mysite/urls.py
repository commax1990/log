from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('polls.urls')),
                  path('dashboard/', include('dashboard.urls'), name='dashboard'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
