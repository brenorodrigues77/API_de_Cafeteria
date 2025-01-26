from typeCoffe.models import typeCoffe
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from typeCoffe.serializers import typeCoffeserializers
from app.permissions import globalDefaultPermission

#view de lista e criação de novos dados
class typeCoffeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission, )
    queryset = typeCoffe.objects.all()
    serializer_class = typeCoffeserializers

#view de alteração, atualização e exclusão de dados
class typeCoffeRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = typeCoffe.objects.all()
    serializer_class = typeCoffeserializers
