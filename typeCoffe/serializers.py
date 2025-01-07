from rest_framework import serializers
from typeCoffe.models import typeCoffe

class typeCoffeserializers(serializers.ModelSerializer):
    class Meta:
        model = typeCoffe
        fields = '__all__'