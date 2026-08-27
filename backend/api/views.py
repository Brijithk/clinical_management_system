# from django.shortcuts import render
# from django.http import JsonResponse
from doctor.models import Consultation
from .serializers import ConsultationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def cmsView(request):
    if request.method=='GET':
        consultation=Consultation.objects.all()
        serializer=ConsultationSerializer(consultation,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)