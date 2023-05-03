from rest_framework import generics
from .models import Tour
from .serializers import TourRetrieveSerializer, TourListSerializer


class TourListAPIView(generics.ListAPIView):
    serializer_class = TourListSerializer

    def get_queryset(self):
        queryset = Tour.objects.all()
        popular = self.request.GET.get('popular')
        best = self.request.GET.get('best')
        if popular:
            queryset = queryset.filter(is_popular=True)
        if best:
            queryset = queryset.filter(is_bestdeal=True)
        return queryset


class TourRetrieveAPIView(generics.ListAPIView):
    serializer_class = TourRetrieveSerializer
    queryset = Tour.objects.all()
    lookup_field = 'pk'
