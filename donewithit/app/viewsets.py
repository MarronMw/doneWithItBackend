from rest_framework import routers, serializers, viewsets
from .serializers import ListingSerializer
from .models import Listings

#write your serializer viewsets herer and do not forget to register it into the urls later 

# ViewSets define the view behavior.
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listings.objects.all()
    serializer_class = ListingSerializer