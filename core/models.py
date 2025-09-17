from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    featured_image = models.ImageField(upload_to='events/', blank=True, null=True)
    swim_type = models.CharField(max_length=50, default='Lake')
    bike_type = models.CharField(max_length=50, default='Rolling')
    run_type = models.CharField(max_length=50, default='Flat')
    temp_high = models.IntegerField(default=23)
    temp_water = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.name} - {self.date}"

class Activity(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return f"{self.title} ({self.start_time.strftime('%Y-%m-%d %H:%M')})"

class Photo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or f"Photo {self.id} for {self.event.name}"

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsors/')

class RecommendedRace(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recommended/')
    link = models.URLField()