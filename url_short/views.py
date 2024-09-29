from rest_framework.request import Request
from rest_framework import status,decorators
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.shortcuts import redirect
from .serializer import UrlSerializer, UrlStatsSerializer
from rest_framework import viewsets
from .models import Url
import shortuuid



class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    lookup_field = 'shortcode'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            name = serializer.validated_data.get('shortcode') or shortuuid.ShortUUID().random(length=6)

            if len(name) < 6:
                additional_length = 6 - len(name)
                name += shortuuid.ShortUUID().random(length=additional_length)

            url_instance, created = Url.objects.get_or_create(url=url, defaults={'shortcode': name})
            if created:
                return Response({'shortcode': url_instance.shortcode}, status=status.HTTP_201_CREATED)
            return Response({'error': 'URL already exists with this shortcode'}, status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        shortcode = kwargs.get(self.lookup_field)
        try:
            short_url = self.get_object()
            serializer = self.get_serializer(short_url)
            return Response(serializer.data)
        except Url.DoesNotExist:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve_stats(self, request, *args, **kwargs):
        shortcode = kwargs.get(self.lookup_field)
        try:
            short_url = self.get_object()
            serializer = UrlStatsSerializer(short_url)
            return Response(serializer.data)
        except Url.DoesNotExist:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
        

    def destroy(self, request, *args, **kwargs):
        shortcode = kwargs.get(self.lookup_field)
        try:
            short_url = self.get_object()
            short_url.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Url.DoesNotExist:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, *args, **kwargs):
        shortcode = kwargs.get(self.lookup_field)
        try:
            short_url = self.get_object()
            serializer = self.get_serializer(short_url, data=request.data, partial=kwargs.pop('partial', False))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Url.DoesNotExist:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def redirect_to(self, request, shortcode):
        try:
            obj_url = Url.objects.get(shortcode=shortcode)
            obj_url.counter += 1
            obj_url.save()
            return redirect(obj_url.url)
        except Url.DoesNotExist:
            return Response({'error': 'URL not found'}, status.HTTP_404_NOT_FOUND)
        
