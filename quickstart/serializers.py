# app_name/serializers.py
from rest_framework import serializers
from quickstart.models import ClassName, Tag, Operator

class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class OperatorSerializer(serializers.ModelSerializer):
    class_name = serializers.SlugRelatedField(slug_field='name', queryset=ClassName.objects.all(), allow_null=True)
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all())

    class Meta:
        model = Operator
        fields = '__all__'
