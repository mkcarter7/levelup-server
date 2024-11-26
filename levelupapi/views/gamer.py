"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Gamer


class GamerView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        
        Returns:
            Response -- JSON serialized game type
        """
        try:
            gamer = Gamer.objects.get(pk=pk)
            serializer = GamerSerializer(gamer)
            return Response(serializer.data)
        except Gamer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        gamers = Gamer.objects.all()
        
        uid = request.query_params.get('uid', None)
        if uid is not None:
            gamers = gamers.filter(uid=uid)
    
        serializer = GamerSerializer(gamers, many=True)
        return Response(serializer.data)
      
    def destroy(self, request, pk):
      gamer = Gamer.objects.get(pk=pk)
      gamer.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)

class GamerSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Gamer
        fields = ('uid', 'bio')
        depth = 1
