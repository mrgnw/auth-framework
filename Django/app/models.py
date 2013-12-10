from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

PRIVATE_CHOICES = (
    (1, 'Yes'),
    (0, 'No'),
)

ARCHIVE_CHOICES = (
    (1, 'Yes'),
    (0, 'No'),
)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    ''' Creates a token whenever a User is created '''
    if created:
        Token.objects.create(user=instance)


class Address(models.Model):
    ''' Model features for an address '''
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.street, self.city, self.state)

    class Meta:
        verbose_name_plural = 'Address'

class RecipeList(models.Model):
    recipe_list_id = models.AutoField(primary_key=True)
    recipe_list_name = models.CharField(max_length=100)
    created = models.DateTimeField()

    def __unicode__(self):
        return self.recipe_list_name

    class Meta:
        ordering = ('created',)


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100)
    frequency = models.IntegerField()
    created = models.DateTimeField()

    def __unicode__(self):
        return self.tag_name

    class Meta:
        ordering = ('created',)


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=0)
    tag = models.ForeignKey(Tag)
    recipe_lists = models.ManyToManyField(RecipeList) # Add a default list?
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.CharField(max_length=4000, blank=True, null=True)
    recipe_directions = models.CharField(max_length=4000, blank=True, null=True)
    recipe_notes = models.CharField(max_length=4000, blank=True, null=True)
    recipe_yield = models.CharField(max_length=20, blank=True, null=True)
    recipe_prep_time = models.IntegerField(blank=True, null=True)
    recipe_cook_time = models.IntegerField(blank=True, null=True)
    recipe_total_time = models.IntegerField(blank=True, null=True)
    recipe_source = models.CharField(max_length=255, blank=True, null=True)
    private = models.BooleanField(choices=PRIVATE_CHOICES,default=1)
    archive = models.BooleanField(choices=ARCHIVE_CHOICES,default=1)
    created = models.DateTimeField(auto_now_add=True) # auto_now_add=True


    def __unicode__(self):
        return self.recipe_name

    class Meta:
        ordering = ('created',)


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe)
    measurement = models.IntegerField()
    measurement_type = models.CharField(max_length=10)

    def __unicode__(self):
        return self.ingredient_name

    class Meta:
        ordering = ('ingredient_name',)


class Image(models.Model):
   image = models.ImageField(upload_to="/Django/images")

   def __unicode__(self):
       return self.image.url