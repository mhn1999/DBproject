from .models import Person,Child,Class,Teacher
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields =['SSN', 'phoneNumber','gender', 'address',
                  'familyName']
class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teacher
		fields =['SSN', 'phoneNumber','gender', 'address',
                  'familyName','contract_type','contract_number','contract_salary','degree']
class ChildSerializer(serializers.ModelSerializer):
	age=serializers.ReadOnlyField()
	class Meta:
		model = Child
		fields =['childID', 'classes','parents', 'hobbies', 'name',
                  'familyName','birthDate', 'age']
class ClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = Class
		fields =['classNumber', 'teachers','price', 'year',
                  'subject']		