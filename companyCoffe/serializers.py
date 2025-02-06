from django.db.models import Avg
from rest_framework import serializers
from companyCoffe.models import companyCoffe

class CompanyCoffeSerializers(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = companyCoffe
        fields = '__all__'

    def get_rate(self, obj):
        rate = round(obj.review.aggregate(Avg('stars'))['stars__avg'], 1)
        if rate:
            return rate
        return None

    def validate_release_date(self, value):
        if value.year < 1950:
          raise serializers.ValidationError('A data de criação nao pode ser menor que 1950.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O campo resumo nao pode ter mais que 500 caracteres.')
        return value
    
    def validate_title(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('O campo titulo nao pode ter mais que 100 caracteres.')
        return value
