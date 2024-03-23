from django.shortcuts import render
from.models import Employee,Punchin,Late_Punchin
from.serializer import Employeeserializer,Punchinserializer,Late_Punchinserializer
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
        current_date=datetime.date.today()
        empid=request.data['empid']
        empname=request.data['empname']
        login_time=datetime.datetime.now()
        try:
            logout_time = datetime.datetime.now()
            if Punchin.objects.filter(empid=empid,logout_time='0').exists():
                logout_data=Punchin.objects.filter(empid=empid,logout_time='0')
                serializer=Punchinserializer(logout_data,many=True)
                t=datetime.date.today()
                y=t.strftime('20%y-%m-%d')
                if serializer.data[0]['current_date'] != y:
                    late_login=serializer.data[0]['login_time']
                    late_details=Late_Punchin(current_date=current_date,empid=empid,empname=empname,login_time=late_login,logout_time=login_time)
                    late_details.save()
                    Punchin.objects.filter(empid=empid, logout_time='0').delete()
                    return Response({"msg" : "logout failed Contact hr"})
                Punchin.objects.filter(empid=empid,logout_time='0').update(logout_time=logout_time)
                return Response({'msg':"logout succesfull"})
        except:
            pass
        save_data=Punchin(current_date=current_date,empid=empid,empname=empname,login_time=login_time)
        save_data.save()
        return Response({'msg':"login","details":"serializer.data"})


@api_view(['POST','GET','PUT','DELETE'])
def Attendance_list(request):
    if request.method=='GET':
        start_date='2024-03-23'
        end_date='2024-03-24'
        s=Punchin.objects.all()
        filtered_list={}
        serializer=Punchinserializer(s,many=True)
        for ch in serializer.data:
            if ch['current_date']>=start_date  and ch['current_date']< end_date:
                if ch['empid'] in filtered_list:
                    empid=ch['empid']
                    filtered_list[empid]['count']=(filtered_list[empid].get('count'))+1
                else:
                    ch['count']=1
                    filtered_list[ch['empid']]=ch
        return Response({'msg':filtered_list})



