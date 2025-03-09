from django.db.models import Avg
from rest_framework import serializers
from companyCoffe.models import companyCoffe
from typeCoffe.serializers import TypeCoffeserializers
from descriptionCoffe.serializers import DescriptionCoffeSerializers


class CompanyCoffeSerializers(serializers.ModelSerializer):

    class Meta:
        model = companyCoffe
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError(
                'A data de criação nao pode ser menor que 1950.')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                'O campo resumo nao pode ter mais que 500 caracteres.')
        return value

    def validate_title(self, value):
        if len(value) > 100:
            raise serializers.ValidationError(
                'O campo titulo nao pode ter mais que 100 caracteres.')
        return value


class CompanyCoffeListDetailSerializers(serializers.ModelSerializer):
    descriptioncoffe = DescriptionCoffeSerializers(many=True)
    typecoffe = TypeCoffeserializers()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = companyCoffe
        fields = ['title', 'typecoffe', 'release_date',
                  'descriptioncoffe', 'resume', 'rate']

    def get_rate(self, obj):
        rate = (obj.review.aggregate(Avg('stars'))['stars__avg'])
        if rate:
            return round(rate, 1)
        return None
