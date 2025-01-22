from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from descriptionCoffe.models import descriptionCoffe
from descriptionCoffe.serializers import descriptionCoffeSerializers

#view de lista e criação de novos dados
class descriptionCoffeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = descriptionCoffe.objects.all()
    serializer_class = descriptionCoffeSerializers

#view de alteração, atualização e exclusão de dados
class descriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = descriptionCoffe.objects.all()
    serializer_class = descriptionCoffeSerializers