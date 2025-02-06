from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from descriptionCoffe.models import descriptionCoffe
from descriptionCoffe.serializers import DescriptionCoffeSerializers
from app.permissions import globalDefaultPermission

#view de lista e criação de novos dados
class DescriptionCoffeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = descriptionCoffe.objects.all()
    serializer_class = DescriptionCoffeSerializers

#view de alteração, atualização e exclusão de dados
class DescriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,) 
    queryset = descriptionCoffe.objects.all()
    serializer_class = DescriptionCoffeSerializers