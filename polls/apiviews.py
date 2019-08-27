#from rest_framework.views import APIView
#from rest_framework.response import Response
#from django.shortcuts import get_object_or_404
from rest_framework import generics
from polls import models
from polls import serializers

# Example codes given below are written with APIView. Now we are goint to
# achieve the same using DRF generic views. So comment the following codes

# class PollList(APIView):
#      def get(self, request):
#          """Get the list of first 20 Polls"""
#          polls = models.Poll.objects.all()[:20]
#          data = serializers.PollSerializer(polls, many=True).data
#          return Response(data)
#
# class PollDetail(APIView):
#     def get(self, request, pk):
#         """Get detail of a Poll"""
#         poll = get_object_or_404(models.Poll, pk=pk)
#         data = serializers.PollSerializer(poll).data
#         return Response(data)

# Example codes with DRF generics views
class PollList(generics.ListCreateAPIView):
    """ListCreateAPIView(allowed methods) - GET, POST"""
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer

class PollDetail(generics.RetrieveDestroyAPIView):
    """RetrieveDestroyAPIView(allowed methods) - GET, DELETE"""
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer

class ChoiceList(generics.ListCreateAPIView):
    """ListCreateAPIView(allowed methods) - GET, POST"""
    queryset = models.Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer

class CreateVote(generics.CreateAPIView):
    """CreateAPIView(allowed methods) - POST"""
    serializer_class = serializers.VoteSerializer
