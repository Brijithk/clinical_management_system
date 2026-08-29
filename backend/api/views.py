# from django.shortcuts import render
# from django.http import JsonResponse
from doctor.models import Consultation
from .serializers import ConsultationSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from administrator.models import User
from django.http import Http404
# Create your views here.

@api_view(['GET','POST'])
def cmsView(request):
    if request.method=='GET':
        consultation=Consultation.objects.all()
        serializer=ConsultationSerializer(consultation,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=ConsultationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def consultationDetailView(request,pk):
    try:
        consultation=Consultation.objects.get(pk=pk)
    except Consultation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= ConsultationSerializer(consultation)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer =ConsultationSerializer(consultation,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        consultation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#administrator

class UserView(APIView):
    def get(self,request):
        user = User.objects.all()
        serializer =  UserSerializer(user,many=True)   
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        user = self.get_object(pk)
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP200)
            