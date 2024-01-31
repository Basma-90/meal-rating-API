from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

class Meal (models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=400)
    def __str__(self):
        return self.title

class Rating(models.Model):
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    meal=models.ForeignKey(Meal,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.meal.title

class Meta:
    unique_together=(('user','meal'),)
    index_together=(('user','meal'),)




