from typeCoffe.models import typeCoffe
from rest_framework import generics
from typeCoffe.serializers import typeCoffeserializers

#view de lista e criação de novos dados
class typeCoffeCreateListView(generics.ListCreateAPIView):
    queryset = typeCoffe.objects.all()
    serializer_class = typeCoffeserializers

#view de alteração, atualização e exclusão de dados
class typeCoffeRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = typeCoffe.objects.all()
    serializer_class = typeCoffeserializers
