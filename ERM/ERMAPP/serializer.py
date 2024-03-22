from rest_framework import serializers
from.models import Employee,Punchin,Late_Punchin


class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class Punchinserializer(serializers.ModelSerializer):
    class Meta:
        model=Punchin
        fields='__all__'

class Late_Punchinserializer(serializers.ModelSerializer):
    class Meta:
        model=Late_Punchin
        fields='__all__'