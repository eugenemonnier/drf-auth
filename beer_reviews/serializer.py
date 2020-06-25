from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ['id', 'author', 'beer_name', 'body']
    model = Review