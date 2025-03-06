from rest_framework import serializers
from reviewCoffe.models import reviewCoffe


class ReviewCoffeserializers(serializers.ModelSerializer):
    class Meta:
        model = reviewCoffe
        fields = '__all__'
