from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField



def image_upload_to(instance, filename):
   name = instance.properties.name
   slug = slugify(name)
   return 'property_img/%s/%s' %(slug, filename)

class Properties(models.Model):
   name = models.CharField(max_length=150)
   slug = models.SlugField(max_length=160)
   bathrooms = models.PositiveIntegerField(blank=True, null=True)
   bedrooms = models.PositiveIntegerField(blank=True, null=True)
   price = models.DecimalField(max_digits=20, decimal_places=2)
   discount_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
   location = models.CharField(max_length=100, blank=True, null=True)
   available = models.BooleanField(default=True)
   is_featured = models.BooleanField(default=False)
   is_new = models.BooleanField(default=True)
   description = RichTextField(blank=True, null=True)
   display_img = models.ImageField(default='default.png', upload_to='display_img')
   created = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return self.name
   
   def get_absolute_url(self):
      return reverse("detail-page", kwargs={
         'pk': self.pk,
         'slug': self.slug,
      })
 
class PropertyImage(models.Model):
   properties = models.ForeignKey(Properties, on_delete=models.CASCADE)
   image = models.ImageField(upload_to=image_upload_to)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
