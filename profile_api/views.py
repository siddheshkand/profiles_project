from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profile_api.serializers import HelloSerializers, UserProfileSerializer, ProfileFeedItemSerializer
from rest_framework import status
from rest_framework import viewsets
from profile_api.models import *
from profile_api import permmisions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = HelloSerializers

    def get(self, request, format=None):
        """:return a list of APIView"""
        an_apiview = [
            'Uses http function as function GET, POST, PUT, DELETE.',
            'Similar to Django class based views.',
            'Gives control over your logic.',
            'It is mapped manually to url',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Hello message with our name"""
        serializer = HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Update the object"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Partially update"""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """delete"""
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = HelloSerializers

    def list(self, request):
        """Return hello message"""

        a_viewset = [
            'Uses action .....',
            'Automatically maps  to url via router ',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create new hello thing"""
        serializer = HelloSerializers(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0} ".format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})


class UserProfileViewset(viewsets.ModelViewSet):
    """ Handles CRUD of Profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permmisions.UpdateOwnProfile]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'name')


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use Obtain token view to validate and create token"""
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = [permmisions.PostOwnStatus, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
