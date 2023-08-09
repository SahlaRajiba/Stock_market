from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    type=models.CharField(max_length=90)

class expert(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=90)
    lastname=models.CharField(max_length=90)
    place=models.CharField(max_length=90)
    post=models.CharField(max_length=90)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=90)

class user(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=90)
    lastname=models.CharField(max_length=90)
    place=models.CharField(max_length=90)
    post=models.CharField(max_length=90)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=90)

class rating(models.Model):
    uid=models.ForeignKey(user,on_delete=models.CASCADE)
    eid=models.ForeignKey(expert,on_delete=models.CASCADE)
    rating=models.IntegerField()
    review=models.CharField(max_length=90)
    date=models.DateField()

class tips(models.Model):
    eid=models.ForeignKey(expert,on_delete=models.CASCADE)
    tips=models.CharField(max_length=90)
    date=models.DateField()

class doubt(models.Model):
    eid=models.ForeignKey(expert,on_delete=models.CASCADE)
    uid=models.ForeignKey(user,on_delete=models.CASCADE)
    doubt=models.CharField(max_length=90)
    reply=models.CharField(max_length=90)
    date=models.DateField()

class notification(models.Model):
    eid=models.ForeignKey(expert,on_delete=models.CASCADE)
    notificaion=models.CharField(max_length=90)
    date=models.DateField()
    time=models.TimeField()

class complaint(models.Model):
    uid=models.ForeignKey(user,on_delete=models.CASCADE)
    notificaion=models.CharField(max_length=90)
    date=models.DateField()
    reply=models.CharField(max_length=90)





