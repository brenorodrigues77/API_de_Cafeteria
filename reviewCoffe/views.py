from rest_framework import generics
from reviewCoffe.models import reviewCoffe
from rest_framework.permissions import IsAuthenticated
from reviewCoffe.serializers import ReviewCoffeserializers
from app.permissions import globalDefaultPermission

#view de lista e criação de novos dados
class ReviewCoffeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = reviewCoffe.objects.all()
    serializer_class = ReviewCoffeserializers

#view de alteração, atualização e exclusão de dados
class ReviewCoffeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = reviewCoffe.objects.all()
    serializer_class = ReviewCoffeserializers

