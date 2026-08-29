from rest_framework import serializers
from doctor.models import Consultation
from administrator.models import User

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consultation
        fields="__all__"


#administrator
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"