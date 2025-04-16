from rest_framework import routers, serializers, viewsets
from .models import Listings

#write your serializers here
class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listings
        fields = ['id','title','price','image']
