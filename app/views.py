from django.shortcuts import render
from app.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import *

# Create your views here.
@api_view()
def EmployeeJData(request):
    EQS=Employee.objects.all()
    ESD=EmployeeMS(EQS,many=True)
    return Response(ESD.data)


