from app.viewsets import ListingViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# defining the default Api urls and the routes
router = routers.DefaultRouter()

# add or register api routes here
router.register(r'listings', ListingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ap/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('', include('app.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
