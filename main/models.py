from django.db import models


class Tour(models.Model):
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    price = models.IntegerField()
    is_bestdeal = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    image_big = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.location


class TourDate(models.Model):
    date = models.CharField(max_length=100)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_dates')
    price_usd = models.PositiveIntegerField()
    price_sum = models.PositiveIntegerField()

    def __str__(self):
        return self.date


class TourDetail(models.Model):
    title = models.CharField(max_length=1000)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_details')
    content = models.TextField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class TourDropDown(models.Model):
    name = models.CharField(max_length=500)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_dropdown')
    text = models.TextField()

    def __str__(self):
        return self.name
