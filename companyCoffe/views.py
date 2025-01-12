from rest_framework import generics
from companyCoffe.models import companyCoffe
from companyCoffe.serializers import companyCoffeSerializers

#view de lista e criação de novos dados
class companyCoffeCreateListView(generics.ListCreateAPIView):
    queryset = companyCoffe.objects.all()
    serializer_class = companyCoffeSerializers

#view de alteração, atualização e exclusão de dados
class companyCoffeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = companyCoffe.objects.all()
    serializer_class = companyCoffeSerializers