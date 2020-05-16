from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    image = models.FileField(blank=True, upload_to='images', default='images/avatar.svg')
    about = models.TextField(max_length=1000)
    logo = models.FileField(blank=True, null=True, upload_to='images')
    resume = models.FileField(blank=True, null=True, upload_to='images')

    class Meta:
        verbose_name_plural = "Person"
    
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
    overview = models.TextField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images')
    priority = models.IntegerField(unique=True)
    project_skills = models.ManyToManyField('Skilltag', blank=True)

    class Meta:
        ordering = ["priority"]

    def __str__(self):
        return self.title


class Skilltag(models.Model):
    skill = models.CharField(max_length=20)

    def __str__(self):
        return self.skill


# Also have to add support for flaticons
class Skill(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=300)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    priority = models.IntegerField(default=0)

    class Meta:
        ordering = ["priority"]

    def __str__(self):
        return self.title



class Experience(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images')
    priority = models.IntegerField(default=0)
    experience_skills = models.ManyToManyField('Skilltag', blank=True)

    class Meta:
        ordering = ["priority"]

    def __str__(self):
        return self.title



class SocialMedia(models.Model):
    name = models.CharField(max_length=500)
    name_fa = models.CharField(max_length=500)
    link = models.URLField()

    def __str__(self):
        return self.name