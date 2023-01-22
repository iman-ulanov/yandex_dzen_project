from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import AuthorRegisterSerializer
from .models import Author


class AuthorRegisterAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer


