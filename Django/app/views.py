from app.models import *
from app.serializers import *

from rest_framework import generics
from rest_framework.views import APIView
#from rest_framework import permissions

#from django.contrib.auth.models import User


class UserList(generics.ListCreateAPIView):
    """List all users or create a new User"""
    #permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a User instance."""
    #permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer


class AddressList(generics.ListCreateAPIView):
    """List all addresses or create a new Address"""
    #permission_classes = (permissions.IsAuthenticated,)
    model = Address
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete an Address."""
    #permission_classes = (permissions.IsAuthenticated,)
    model = Address
    serializer_class = AddressSerializer


class RecipeList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    model = Recipe
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    model = Recipe
    serializer_class = RecipeSerializer


class TagList(generics.ListCreateAPIView):
    # model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    model = Tag
    serializer_class = TagSerializer


class RecipeListList(generics.ListCreateAPIView):
    from app.models import RecipeList as RL  # There's a naming conflict with the RecipeList class above.
    model = RL  # Consider renaming.
    serializer_class = RecipeListSerializer


class PhotoDetail(APIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(data=request.DATA, files=request.FILES)
        return Response(serializer.data)

        
