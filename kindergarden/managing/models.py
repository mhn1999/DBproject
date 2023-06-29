
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
    @property
    def class_list(self):
        value_fileds=("classNumber","subject","year")
        return self.teacher_set.all().values(*value_fileds)

class Class(models.Model):
    classNumber=models.BigAutoField(primary_key=True)
    subject= models.CharField(max_length=200)
    year = models.IntegerField()
    price= models.IntegerField()
    teachers=models.ManyToManyField(Teacher, related_name="teacher_set")
    def __str__(self):
        return self.subject 
    @property
    def children_list(self):
        value_fileds=("childID","name","familyName")
        return self.children.all().values(*value_fileds) 
    @property
    def teacher_list(self):
        value_fileds=("SSN","name","familyName",'degree')
        return self.teachers.all().values(*value_fileds)
# Create your models here.
class Child(models.Model):

    #id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    childID = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200)
    familyName=models.CharField(max_length=200)
    hobbies=models.CharField(max_length=200,null=True, blank=True)
    birthDate=models.DateTimeField()
    #category=models.CharField
    classes=models.ManyToManyField(Class, related_name="children")
    parents=models.ManyToManyField(Person)
    def __str__(self):
        return self.name
    @property
    def parent_list(self):
        value_fileds=("SSN","name","familyName")
        return self.parents.all().values(*value_fileds)
    @property
    def class_list(self):
        value_fileds=("classNumber","subject","year","price")
        return self.classes.all().values(*value_fileds)
    @property
    def age(self):
        return int(datetime.date.today().year)-int(self.birthDate.year)
