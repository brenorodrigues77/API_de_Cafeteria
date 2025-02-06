from django.db.models import Count, Avg 
from rest_framework import generics, views, response
from companyCoffe.models import companyCoffe
from reviewCoffe.models import reviewCoffe
from rest_framework.permissions import IsAuthenticated
from companyCoffe.serializers import CompanyCoffeSerializers
from app.permissions import globalDefaultPermission

#view de lista e criação de novos dados
class CompanyCoffeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = companyCoffe.objects.all()
    serializer_class = CompanyCoffeSerializers

#view de alteração, atualização e exclusão de dados
class CompanyCoffeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = companyCoffe.objects.all()
    serializer_class = CompanyCoffeSerializers

class CompanyCoffeStatsView(views.APIView):
    permission_classes = (IsAuthenticated, globalDefaultPermission,)
    queryset = companyCoffe.objects.all()
    def get(self, request):
        total = self.queryset.count()
        companycoffe_by_typecoffe = self.queryset.values('typecoffe__name').annotate(count=Count('id'))
        total_reviews = reviewCoffe.objects.count()
        average_stars = reviewCoffe.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(data={
            'total': total,
            'companycoffe_by_typecoffe': companycoffe_by_typecoffe,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }, status=200)