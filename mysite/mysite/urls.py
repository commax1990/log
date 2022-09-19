from dashboard.views import api_table
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api/apidashborad', api_table)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('polls.urls')),
                  path('dashboard/', include('dashboard.urls'), name='dashboard'),
                  # path('api/', include('dashboard.urls'), name='api'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls
