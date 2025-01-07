from typeCoffe.models import typeCoffe
from rest_framework import generics
from typeCoffe.serializers import typeCoffeserializers


class typeCoffeCreateListView(generics.ListCreateAPIView):
    queryset = typeCoffe.objects.all()
    serializer_class = typeCoffeserializers


class typeCoffeRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = typeCoffe.objects.all()
    serializer_class = typeCoffeserializers
