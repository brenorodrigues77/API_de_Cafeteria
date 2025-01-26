from rest_framework import generics
from reviewCoffe.models import reviewCoffe
from rest_framework.permissions import IsAuthenticated
from reviewCoffe.serializers import reviewCoffeserializers
from app.permissions import globalDefaultPermission

#view de lista e criação de novos dados
class reviewCoffeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = reviewCoffe.objects.all()
    serializer_class = reviewCoffeserializers

#view de alteração, atualização e exclusão de dados
class reviewCoffeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = reviewCoffe.objects.all()
    serializer_class = reviewCoffeserializers

