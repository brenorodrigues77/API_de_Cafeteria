from rest_framework import generics
from companyCoffe.models import companyCoffe
from companyCoffe.serializers import companyCoffeSerializers

class companyCoffeCreateListView(generics.ListCreateAPIView):
    queryset = companyCoffe.objects.all()
    serializer_class = companyCoffeSerializers

class companyCoffeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = companyCoffe.objects.all()
    serializer_class = companyCoffeSerializers