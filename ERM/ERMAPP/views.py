from django.shortcuts import render
from.models import Employee,Attendance
from.serializer import Employeeserializer,Attendanceserializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
import datetime


def Empid():
    num=''
    try:
        last=Employee.objects.all()
        serializer=Employeeserializer(last,many=True)
        last_id=serializer.data[-1]['empid']
    except:
        last_id='MT-1000'
    for i in last_id:
        if i in '0123456789':
            num+=i
    num=int(num)+1
    return 'MT-'+str(num)

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


@api_view(['POST','GET','PUT','DELETE'])
def Attendance_data(request):
    if request.method=="POST":
        current_date=datetime.datetime.now()
        empid=request.data['empid']
        empname=request.data['empname']
        login_time=datetime.datetime.now()
        try:
            logout_time=datetime.datetime.now()
            last_attend=Attendance.objects.filter(empid=empid).last()
            serializer=Attendanceserializer(last_attend)
            if serializer.data['logout_time']=='0':
                Attendance.objects.filter(logout_time='0').update(logout_time=logout_time)
                return Response({'msg':"logout succesfull"})
        except:
            pass
        save_data=Attendance(current_date=current_date,empid=empid,empname=empname,login_time=login_time)
        save_data.save()
        return Response({'msg':"login","details":"serializer.data"})

