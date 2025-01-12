from rest_framework import serializers
from reviewCoffe.models import reviewCoffe

class reviewCoffeserializers(serializers.ModelSerializer):
    class Meta:
        model = reviewCoffe
        fields = '__all__'