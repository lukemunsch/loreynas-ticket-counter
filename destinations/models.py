from django.db import models
from django.template.defaultfilters import slugify


class Area(models.Model):
    """set up our top level class for the areas models"""
    area_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    area_description = models.TextField()
    friendly_area_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    class Meta:
        """set up how the order works for the areas"""
        ordering = ['area_name']

    def __str__(self):
        return self.area_name

    def get_friendly_area_name(self):
        """return a value for our friendly name"""
        return self.friendly_area_name


class District(models.Model):
    """set up a sub area model for extra filtering"""
    district_name = models.CharField(max_length=100, null=False, blank=False)
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    friendly_district_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.district_name

    def get_friendly_district_name(self):
        """set up the friendly versions of our district names"""
        return self.friendly_district_name


class Destination(models.Model):
    """set up our specific destinations for purchasing"""
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )
    district = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField()
    hotspot = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.area}-{self.name}')
        return super().save(*args, **kwargs)
