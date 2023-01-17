from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import MinionSerializer
import requests
# Create your views here.

# Gateway view to access external API
class GatewayViewSet(viewsets.GenericViewSet):
    permission_classes = []
    serializer_class = None

    # Route to get cep info from external API
    @action(detail=False, methods=['get'], url_path='cep/(?P<cep>[0-9]+)')
    def cep(self, request, cep):
        url = 'https://viacep.com.br/ws/' + cep + '/json/'
        response = requests.get(url).json()
        return Response(response, status=status.HTTP_200_OK)

    # Route to get facts about numbers from external API
    @action(detail=False, methods=['get'], url_path='numbers/(?P<number>[0-9]+)')
    def numfacts(self, request, number):
        url = 'http://numbersapi.com/' + number + '/trivia'
        response = requests.get(url).text
        return Response(response, status=status.HTTP_200_OK)
    
    # Route to translate text to minion language from external API
    @action(detail=False, methods=['post'], serializer_class= MinionSerializer,
            url_path='minion')
    def minion(self, request):
        text = request.data.get('text')
        url = 'https://api.funtranslations.com/translate/minion.json'
        response = requests.post(url, data={'text': text}).json()
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='kanye')
    def kanye(self, request):
        url = 'https://api.kanye.rest/'
        response = requests.get(url).json()
        return Response(response, status=status.HTTP_200_OK)
    
    