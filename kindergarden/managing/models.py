
# Create your models here.
from django.db import models
import datetime
import uuid
from django.db.models.deletion import CASCADE

class Person(models.Model):
    gender_choises=(
        ("0","female"),
        ("1","male")
    )
    SSN=models.BigAutoField(primary_key=True)
    phoneNumber=models.IntegerField(blank=True,null=True)
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,choices=gender_choises)
    address=models.TextField()
    familyName=models.CharField(max_length=200)
    def __str__(self):
        return str(self.SSN)

class Teacher(Person):
    contract_types=(
        ("a","hourly"),
        ("b", "contractly")
    )
    contract_type=models.CharField(max_length=200 , choices=contract_types)
    contract_salary=models.IntegerField()
    contract_number=models.IntegerField(unique=True)
    degree=models.CharField(max_length=200)

class Class(models.Model):
    classNumber=models.BigAutoField(primary_key=True)
    subject= models.CharField(max_length=200)
    year = models.IntegerField()
    price= models.IntegerField()
    teachers=models.ManyToManyField(Teacher)
    def __str__(self):
        return self.subject    
# Create your models here.
class Child(models.Model):

    #id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    childID = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200)
    familyName=models.CharField(max_length=200)
    hobbies=models.CharField(max_length=200,null=True, blank=True)
    birthDate=models.DateTimeField()
    #category=models.CharField
    classes=models.ManyToManyField(Class)
    parents=models.ManyToManyField(Person)
    def __str__(self):
        return self.name
    
    @property
    def age(self):
        return int(datetime.date.today().year)-int(self.birthDate.year)
