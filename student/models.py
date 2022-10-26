from django.db import models
from django.contrib.auth.models import User

class ClassName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    @property
    def get_name(self):
        return self.name
    

class Batch(models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(ClassName, on_delete=models.DO_NOTHING,null=False)
    name = models.TextField(max_length=200)
    @property
    def get_name(self):
        return self.name +" - "+ self.class_id.name
    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassName, on_delete=models.DO_NOTHING,null=False)
    batch_id = models.ForeignKey(Batch, on_delete=models.DO_NOTHING,null=False)
    profile_pic= models.ImageField(upload_to='profile_pic/Student/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    monthly_fee = models.IntegerField(null=False)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name+" "+self.user.class_id.name+" "+self.user.batch_id.name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
