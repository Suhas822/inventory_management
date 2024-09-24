from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.transaction import atomic
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer, UserRegisterSerializer


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user = User.objects.create_user(
            username=request.data["username"], password=request.data["password"]
        )
        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )


class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        item_name = request.data.get("name")
        if Item.objects.filter(name=item_name).exists():
            return Response(
                {"error": "Item already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    @atomic
    def retrieve(self, request, *args, **kwargs):
        item_id = kwargs.get("pk")
        cached_item = cache.get(f"item:{item_id}")

        if cached_item:
            return Response(cached_item)

        try:
            item = self.get_object()
        except Http404:
            return Response(
                {"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(item)
        cache.set(f"item:{item_id}", serializer.data, timeout=60 * 15)
        return Response(serializer.data)

    @atomic
    def update(self, request, *args, **kwargs):
        item_id = kwargs.get("pk")
        try:
            item = self.get_object()
        except Http404:
            return Response(
                {"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            cache.delete(f"item:{item_id}")
            cache.set(f"item:{item_id}", serializer.data, timeout=60 * 15)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @atomic
    def destroy(self, request, *args, **kwargs):
        item_id = kwargs.get("pk")
        try:
            item = self.get_object()
        except Http404:
            return Response(
                {"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND
            )
        self.perform_destroy(item)
        cache.delete(f"item:{item_id}")

        return Response(
            {"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
