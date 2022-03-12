from django.shortcuts import render

from django.shortcuts import get_object_or_404
# from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import CandidateSerializer
from .models import Candidate
from rest_framework.pagination import PageNumberPagination

from .producer import publish

class CandidateViewSet(viewsets.ViewSet):
    def list(self, request):
        location = request.GET.get('location')
        skill = request.GET.get('tech_skills')
        pagination_class = PageNumberPagination
        if location and skill:
            response = Candidate.objects.filter(location__icontains=location,tech_skills__icontains=skill)
        elif location:
            response = Candidate.objects.filter(location__icontains=location)
        elif skill:
            response = Candidate.objects.filter(tech_skills__icontains=skill)
        else:
            response = Candidate.objects.all()
        serializer = CandidateSerializer(response, many=True)

        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
    def retrieve(self, request, pk=None):
        pass

    def create(self, request):
        try:
            print('start posting candidate')
            # revyz-bucket
            serializer = CandidateSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save(raise_exception=True)
                publish('candidate_created',serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)