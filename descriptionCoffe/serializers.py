from rest_framework import serializers
from descriptionCoffe.models import descriptionCoffe

class DescriptionCoffeSerializers(serializers.ModelSerializer):
    class Meta:
        model = descriptionCoffe
        fields = '__all__'
