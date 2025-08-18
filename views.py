from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer
import logging

# Configuring logging
logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_menu_item(request, pk):
    """
    API view to handle fetching a particular menu from the database
    """
    try:
        menu_item = MenuItem.objects.get(pk=pk)
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except ObjectDoesNotExist:
        return Response(
            {"error": "Menu item not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    except Exception as e:
        # Log the error for debugging
        logger.error(f"Unexpected error fetching menu item {pk}: {e}")
        return Response(
            {"error": "Something went wrong. please try again later."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )