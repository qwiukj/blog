from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class NewUser(AbstractUser):
    usex = models.BooleanField(default=True)
    uage = models.IntegerField(default=0)
    uphone = models.CharField(max_length=11, default='')
    tags = models.ManyToManyField(Tag, blank=True)
    profile = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.username


    class Meta(AbstractUser.Meta):
        pass

