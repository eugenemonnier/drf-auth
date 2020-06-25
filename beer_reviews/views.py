from rest_framework import generics

from .models import Review
from .permissions import IsAuthorOrReadOnly
from .serializer import ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
