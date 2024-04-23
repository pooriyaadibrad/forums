from django.db import models

# Create your models here.

"""
this place we create models for posts and cattegory for every post
"""
class post(models.Model):
    title = models.CharField(max_length=100,default='',null=False,blank=False)
    #author = models.CharField(max_length=100,default='',null=False,blank=False)
    content = models.TextField(default='',null=True,blank=True)
    image = models.ImageField(upload_to='media/post/',default='default.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title} , {self.pub_date}'
class category(models.Model):
    name = models.CharField(max_length=100,default='',null=False,blank=False)
    def __str__(self):
        return f'{self.name}'


"""
this place you can create custom user models for every post for every category and create assiciated model for every post
class users(models.Model):
    name = models.CharField(max_length=100,default='',null=False,blank=False)
    password = models.CharField(max_length=100,default='',null=False,blank=False)
    email = models.CharField(max_length=100,default='',null=False,blank=False)
    def __str__(self):
        return f'{self.name}'
"""


