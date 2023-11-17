from django.db import models

class ClassName(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Operator(models.Model):
    RARITY_CHOICES = [
        (1, '1-Star'),
        (2, '2-Star'),
        (3, '3-Star'),
        (4, '4-Star'),
        (5, '5-Star'),
        (6, '6-Star'),
    ]

    name = models.CharField(max_length=255, unique=True)
    rarity = models.IntegerField(choices=RARITY_CHOICES)
    class_name = models.ForeignKey(ClassName, on_delete=models.SET_NULL, null=True)
    # image = models.ImageField(upload_to='operator_images/')
    tags = models.ManyToManyField(Tag, related_name='operators')

    def __str__(self):
        return self.name
