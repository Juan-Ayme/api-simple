from projects.models import Productor
from rest_framework import viewsets,permissions
from .serializers import ProductorSerializer

class ProductorViewSert(viewsets.ModelViewSet):
    queryset = Productor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductorSerializer
