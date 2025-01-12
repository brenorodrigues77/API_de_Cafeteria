from rest_framework import generics
from descriptionCoffe.models import descriptionCoffe
from descriptionCoffe.serializers import descriptionCoffeSerializers

#view de lista e criação de novos dados
class descriptionCoffeCreateListView(generics.ListCreateAPIView):
    queryset = descriptionCoffe.objects.all()
    serializer_class = descriptionCoffeSerializers

#view de alteração, atualização e exclusão de dados
class descriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = descriptionCoffe.objects.all()
    serializer_class = descriptionCoffeSerializers