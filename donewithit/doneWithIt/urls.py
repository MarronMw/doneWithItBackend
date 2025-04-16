from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app.viewsets import ListingViewSet

#defining the default Api urls and the routes
router=routers.DefaultRouter()

#add or register api routes here
router.register(r'listings',ListingViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ap/', include('rest_framework.urls')),
    path('api/',include(router.urls)),
    path('',include('app.urls'))
]
