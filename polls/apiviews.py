from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from polls import models
from polls import serializers

class PollList(APIView):
     def get(self, request):
         """Get the list of first 20 Polls"""
         polls = models.Poll.objects.all()[:20]
         data = serializers.PollSerializer(polls, many=True).data
         return Response(data)

class PollDetail(APIView):
    def get(self, request, pk):
        """Get detail of a Poll"""
        poll = get_object_or_404(models.Poll, pk=pk)
        data = serializers.PollSerializer(poll).data
        return Response(data)
