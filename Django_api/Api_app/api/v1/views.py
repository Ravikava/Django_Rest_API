from django.shortcuts import render
from Api_app.models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeApi(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            emp = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EmployeeSerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Update Successfully'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk, format=None):
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Update Successfully'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emp = Employee.objects.get(pk=pk)
        emp.delete()
        return Response({'msg':'Data Deleted Succesfully'}, status=status.HTTP_204_NO_CONTENT)