from rest_framework import viewsets, status, mixins, generics
from rest_framework.response import Response
from .permissions import IsAuthorPermissions
from .serializers import AuthorRegisterSerializer
from .models import Author


class AuthorRegisterAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer
    # permission_classes = [IsAuthorPermissions]


class AuthorRegisterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer
    permission_classes = [IsAuthorPermissions]