from rest_framework import generics
from descriptionCoffe.models import descriptionCoffe
from descriptionCoffe.serializers import descriptionCoffeSerializers


class descriptionCoffeCreateListView(generics.ListCreateAPIView):
    queryset = descriptionCoffe.objects.all()
    serializer_class = descriptionCoffeSerializers

class descriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = descriptionCoffe.objects.all()
    serializer_class = descriptionCoffeSerializers