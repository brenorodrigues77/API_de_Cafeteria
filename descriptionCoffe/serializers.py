from rest_framework import serializers
from descriptionCoffe.models import descriptionCoffe

class descriptionCoffeSerializers(serializers.ModelSerializer):
    class Meta:
        model = descriptionCoffe
        fields = '__all__'
