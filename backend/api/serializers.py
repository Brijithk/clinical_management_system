from rest_framework import serializers
from doctor.models import Consultation,PrescribedLab
from administrator.models import UserProfile

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consultation
        fields="__all__"

class PrescribedLabSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrescribedLab
        fields="__all__"

#administrator
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields="__all__"