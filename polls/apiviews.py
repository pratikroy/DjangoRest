from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
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

class PollViewSet(viewsets.ModelViewSet):
    """Merge the above two functionality into one"""
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer

class ChoiceList(generics.ListCreateAPIView):
    """ListCreateAPIView(allowed methods) - GET, POST"""
    def get_queryset(self):
        queryset = models.Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = serializers.ChoiceSerializer

class CreateVote(APIView):
    """Customized API according to your need"""
    serializer_class = serializers.VoteSerializer

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {
            "choice":choice_pk,
            "poll":pk,
            "voted_by":voted_by
        }
        serializer = serializers.VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
