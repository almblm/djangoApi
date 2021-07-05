# Create your models here.
from django.db import models

class SampleName(models.Model):
    """
    さんぷる
    """
    name = models.CharField('書籍名',max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    bookType = models.CharField('種類',max_length=255)

    def __str__(self):
        return self.name

