from rest_framework import generics
from reviewCoffe.models import reviewCoffe
from reviewCoffe.serializers import reviewCoffeserializers

#view de lista e criação de novos dados
class reviewCoffeCreateListView(generics.ListCreateAPIView):
    queryset = reviewCoffe.objects.all()
    serializer_class = reviewCoffeserializers

#view de alteração, atualização e exclusão de dados
class reviewCoffeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = reviewCoffe.objects.all()
    serializer_class = reviewCoffeserializers

