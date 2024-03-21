from rest_framework import serializers
from.models import Employee,Attendance


class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class Attendanceserializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'