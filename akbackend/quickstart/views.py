from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from akbackend.quickstart.serializers import ClassNameSerializer, TagSerializer, OperatorSerializer


class ClassNameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ClassName.objects.all()
    serializer_class = ClassNameSerializer
    permission_classes = [permissions.IsAuthenticated]


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

class OperatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
    permission_classes = [permissions.IsAuthenticated]