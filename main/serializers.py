from .models import Tour, TourDate, TourDetail, TourDropDown
from rest_framework import serializers


class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'location', 'duration', 'price', 'city', 'image']


class TourDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDate
        fields = ['id', 'date', 'price_usd', 'price_sum']


class TourDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDetail
        fields = ['id', 'title', 'content', 'description', 'image']


class TourDropDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDropDown
        fields = ['id', 'name', 'text']


class TourRetrieveSerializer(serializers.ModelSerializer):
    tour_dates = TourDateSerializer(many=True)
    tour_details = TourDetailSerializer(many=True)
    tour_dropdown = TourDropDownSerializer(many=True)

    class Meta:
        model = Tour
        fields = ['id', 'location', 'duration', 'price', 'city', 'image', 'tour_dates', 'tour_details', 'tour_dropdown']
