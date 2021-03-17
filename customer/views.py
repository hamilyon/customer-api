from django_filters import rest_framework as django_filters
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CompanySerializer, CustomerNoteSerializer, CustomerSerializer
from .models import Company, Customer, CustomerNote

class CustomersFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['company__id', 'firstName', 'lastName', 'status', 'creationDate']


class CustomersFilterList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (django_filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = CustomersFilter
    fields = ('firstName', 'lastName', 'status', 'creationDate')
    filter_fields = fields
    search_fields = fields


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('company')
    serializer_class = CustomerSerializer


class CustomerNoteViewSet(viewsets.ModelViewSet):
    queryset = CustomerNote.objects.all().order_by('customer')
    serializer_class = CustomerNoteSerializer