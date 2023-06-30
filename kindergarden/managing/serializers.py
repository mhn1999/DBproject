from .models import Person,Child,Class,Teacher
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields =['SSN', 'phoneNumber','gender', 'address','name',
                  'familyName']
class TeacherSerializer(serializers.ModelSerializer):
	class_list=serializers.ReadOnlyField()
	class Meta:
		model = Teacher
		fields =['SSN', 'phoneNumber','gender', 'address','name','class_list',
                  'familyName','contract_type','contract_number','contract_salary','degree']
class ChildSerializer(serializers.ModelSerializer):
	parent_list=serializers.ReadOnlyField()
	class_list=serializers.ReadOnlyField()
	age=serializers.ReadOnlyField()
	class Meta:
		model = Child
		fields =['childID', 'class_list','parent_list', 'hobbies', 'name',
                  'familyName','birthDate', 'age', 'parents']
class ClassSerializer(serializers.ModelSerializer):
	children_list=serializers.ReadOnlyField()
	teacher_list=serializers.ReadOnlyField()
	class Meta:
		model = Class
		fields =['classNumber', 'teacher_list','price', 'year','teachers',
                  'subject','children_list']		