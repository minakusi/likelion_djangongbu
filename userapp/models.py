from django.db import models

# Create your models here.
class Userinfo(models.Model):
    userName = models.CharField(max_length = 10)
    FEMALE = "XY"
    MALE = "XX"
    SEX_CHOICES = ((FEMALE, "여자"), (MALE, "남자"))
    userSex = models.CharField(choices = SEX_CHOICES, max_length = 2, null = True, blank = True)
    userIntro = models.TextField(default='')
    
    def __str__(self):
        return self.userName