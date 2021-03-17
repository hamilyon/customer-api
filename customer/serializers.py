# serializers.py

from rest_framework import serializers

from .models import Customer, Company, CustomerNote


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'customers')
        

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'firstName', 'lastName', 'status', 'creationDate', 'company', 'version', 'notes')
        

class CustomerNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerNote
        fields = ('id', 'text', 'customer', 'version',)
        