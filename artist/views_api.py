from rest_framework import serializers, viewsets, status
from .models import Artist
from .serializers import ArtistSerializer, ArtistSaveSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ArtistViewSet(viewsets.ModelViewSet):
    @api_view(['GET', 'POST'])
    def artist_list(self, fomat=None):
        if self.method == 'GET':
            artists = Artist.objects.all()
            artist_serializer = ArtistSerializer(artists, many=True)
            return Response(artist_serializer.data)
        elif self.method == 'POST':
            artist_serializer = ArtistSaveSerializer(data=self.data)
            if artist_serializer.is_valid():
                artist_serializer.save()
                return Response(artist_serializer.data, status=status.HTTP_201_CREATED)
            return Response(artist_serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PUT','DELETE','GET'])
    def artist_detail(self, artistId):
        if self.method == 'PUT':
            artist = Artist.objects.get(pk=artistId)
            artist_serializer = ArtistSerializer(artist, data=self.data)
            if artist_serializer.is_valid():
                artist_serializer.save()
                return Response(artist_serializer.data, status=status.HTTP_201_CREATED)
            return Response(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif self.method == 'DELETE':
            artist.delete()
            return Response({'message': 'Artist was deleted!'}, status=status.HTTP_204_NO_CONTENT)
        elif self.method == 'GET':
            artist_serializer = ArtistSerializer(artist)
            return Response()