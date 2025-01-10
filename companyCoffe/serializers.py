from rest_framework import serializers
from companyCoffe.models import companyCoffe

class companyCoffeSerializers(serializers.ModelSerializer):
    class Meta:
        model = companyCoffe
        fields = '__all__'