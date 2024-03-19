from django.shortcuts import render
from.models import Employee
from.serializer import Employeeserializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
prev1=''
prev=Employee.objects.all()
serializer=Employeeserializer(prev,many=True)
data=serializer.data[-1]['empid']
for i in data:
    if i in '0123456789':
        prev1+=i
prev1=int(prev1)
def Empid():
    global prev1
    new=prev1+1
    prev1=new
    return 'MT-'+str(new)
@api_view(['POST','GET','PUT','DELETE'])
def Employee_data(request):
    if request.method=='POST':
        empid=Empid()
        empname=request.data['empname']
        DOJ=request.data['DOJ']
        email=request.data['email']
        designation=request.data['designation']
        Emp_data=Employee(empid=empid,empname=empname,DOJ=DOJ,email=email,designation=designation)
        Emp_data.save()
        data=Employee.objects.get(empid=empid)
        serializer=Employeeserializer(data)
        return Response(serializer.data)
    #return Response(status=status.HTTP_201_CREATED)

    elif request.method=='GET':
        employee_details=Employee.objects.all()
        serializer =Employeeserializer(employee_details,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='PUT':
        employee_details =Employee.objects.get(empid=request.data['empid'])
        serializer=Employeeserializer(employee_details,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method=='DELETE':
        employee_details =Employee.objects.get(empid=request.data['empid'])
        employee_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)