from rest_framework import generics
from companyCoffe.models import companyCoffe
from rest_framework.permissions import IsAuthenticated
from companyCoffe.serializers import companyCoffeSerializers
from app.permissions import globalDefaultPermission

#view de lista e criação de novos dados
class companyCoffeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = companyCoffe.objects.all()
    serializer_class = companyCoffeSerializers

#view de alteração, atualização e exclusão de dados
class companyCoffeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = companyCoffe.objects.all()
    serializer_class = companyCoffeSerializers