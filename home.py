from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    """
    A view function that fetches the restaurant's name
    from the Restaurant model and displays it in the
    homepage.
    """
    restaurant = Restaurant.objects.first()  # Assuming we have one record of restaurant
    context = {
        "restaurant_name": restaurant.name if restaurant else "Restaurant"
    }

    return render(request, "home.html", context)