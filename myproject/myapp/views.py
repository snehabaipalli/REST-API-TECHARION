from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from myapp.serializers import studentSerializer
# Create your views here.

@api_view(['GET']) # Getting all student informantion
def get_data(request):
    student_obj=student.objects.all()
    serializer=studentSerializer(student_obj,many=True)
    return Response(serializer.data)

@api_view(['POST']) # creating a student
def post_data(request):
    student_obj=student.objects.all()
    seri=studentSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
    return Response(seri.data)

@api_view(['POST']) #updating the data
def update_data(request, id):
    ob=student.objects.get(id=id)
    seri=studentSerializer(instance=ob, data=request.data)
    if seri.is_valid():
        seri.save()
    return Response(seri.data)

@api_view(['DELETE'])
def delete_data(request,id):
    ob=student.objects.get(id=id)
    ob.delete()
    return Response("deleted")

@api_view(['GET']) # getting the marks of a student using id
def get_marks(request,id):
    stu=get_object_or_404(student, pk=id)
    return JsonResponse({'marks':stu.marks})

@api_view(['POST']) # posting the marks
def post_marks(request):
    seri=studentSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
    return Response({'status':'marks posted successfully'})




