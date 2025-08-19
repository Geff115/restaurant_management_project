from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_menu(request):
    """
    This view returns the restaurant's menu. The menu is
    hardcoded for now. In a real implementation, it'll be
    fetched from the database.
    """
    menu = [
        {"name": "Spaghetti and Grilled Turkey", "description": "Classic Italian dish and a marinated turkey", "price": 12.50},
        {"name": "Grilled Salmon", "description": "Fresh salmon fillet with lemon butter sauce", "price": 15.99},
        {"name": "Pizza Margherita", "description": "Classic cheese and tomato pizza", "price": 8.99},
        {"name": "Classic Caesar Salad", "description": "Romaine lettuce, croutons, and Caesar dressing", "price": 7.50},
    ]
    return Response(menu, status=status.HTTP_200_OK)
    