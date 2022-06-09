from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(null=False, blank=False, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
