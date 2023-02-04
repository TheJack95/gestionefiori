from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Item
from .models import ItemSerializer


# Create your views here.

class ItemsView(APIView):

    def get(self, request, *args, **kwargs):
        result = Item.objects.all()
        serializers = ItemSerializer(result, many=True)
        return Response({'status': 'success', 'items': serializers.data}, status=200)
