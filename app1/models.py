from django.db import models
from phone_field import PhoneField
from djmoney.models.fields import MoneyField
from django.conf import settings
import datetime

class ArticleColor(models.Model):
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.color
    

class ArticleGuarantee(models.Model):
    guarantee_time = models.CharField(max_length=50)
    def __str__(self):
        return self.guarantee_time

class ArticleCatagory(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

def upload_path(instance,title):
    today = str(datetime.datetime.now())
    name = instance.user
    return f'images/{name}/{today}.jpg'
    
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path, blank=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ArticleCatagory, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(ArticleColor, on_delete=models.CASCADE)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)
    cost = MoneyField(max_digits=12,decimal_places=2, default_currency='USD')
    guarantee = models.ForeignKey(ArticleGuarantee, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    phone_call = PhoneField()
    def __str__(self):
        return self.title
