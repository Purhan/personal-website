from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images', default='images/avatar.svg')
    
    def save(self, *args, **kwargs):
        if not self.image:
            self.image = 'images/avatar.svg'
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images')
    priority = models.IntegerField(default=0)
    skills = models.ManyToManyField('Skilltag')

    def __str__(self):
        return self.title


class Skilltag(models.Model):
    skill = models.CharField(max_length=20)

    def __str__(self):
        return self.skill