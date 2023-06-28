import re
from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from django.http import JsonResponse, multipartparser
from rest_framework import permissions, status, generics
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .serializers import PersonSerializer, ChildSerializer,TeacherSerializer,ClassSerializer
from django.db.models import Q


from django.core.files.uploadedfile import InMemoryUploadedFile
import base64
import io
from rest_framework.parsers import MultiPartParser,FormParser

from .models import Person,Teacher,Class,Child
# Create your views here.
class AllChildList(APIView):
	def get(self,request):
		book = Child.objects.all()
		serializer = ChildSerializer(book, many=True)
		return Response(serializer.data)
	
class ChildInformation(APIView):
	def get(self,request,pk):
		book = Child.objects.get(childID=pk)
		serializer = ChildSerializer(book, many=False)
		return Response(serializer.data)

class AllClassList(APIView):
	def get(self,request):
		book = Class.objects.all()
		serializer = ClassSerializer(book, many=True)
		return Response(serializer.data)
	
class ClassInformation(APIView):
	def get(self,request,pk):
		book = Class.objects.get(classNumber=pk)
		serializer = ClassSerializer(book, many=False)
		return Response(serializer.data)

class AllTeacherList(APIView):
	def get(self,request):
		book = Teacher.objects.all()
		serializer = TeacherSerializer(book, many=True)
		return Response(serializer.data)
	
class TeacherInformation(APIView):
	def get(self,request,pk):
		book = Teacher.objects.get(SSN=pk)
		serializer = TeacherSerializer(book, many=False)
		return Response(serializer.data)
	
class ClassCreate(APIView):
	def post(self,request):
		serializer = ClassSerializer(data=request.data, partial=True)

		if serializer.is_valid():
			serializer.save()

		return Response({"message": serializer.data})

class ClassUpdate(APIView):

	def post(self,request,pk):
		classObject = [Class.objects.get(classNumber=pk)]
		if 'child_list' in request.data:
			for childId in request.data['child_list']:
				child=Child.objects.get(childID=childId)
				child.classes.add(*classObject)	
				child.save()
		return Response("ok")
	
class ChildCreate(APIView):
	def post(self,request):
		serializer = ChildSerializer(data=request.data, partial=True)

		if serializer.is_valid():
			serializer.save()

		return Response({"message": serializer.data})