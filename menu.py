from django.shortcuts import render

def menu_list(request):
    """
    This view displays a list of hardcoded menu items
    """
    menu_items = [
        {"name": "Jollof Rice & Chicken", "price": "13.50", "description": "Classic jollof made with chicken seasoning, fresh tomatoes, diced beef, marinated chicken, and carrots."},
        {"name": "Pepperoni pizza", "price": "9.50", "description": "Tomato sauce, mozzarella, and spicy pepperoni."},
        {"name": "Chicken & Chips", "price": "11.50", "description": "sweet potato fries or irish potato fries + crunchy spiced chicken or marinated chicken barbecue"},
        {"name": "Veggie Burger", "price": "7.00", "description": "Grilled veggie patty with lettuce, tomato, and vegan mayo."}
    ]

    return render(request, "menu_list.html", {"menu_items": menu_items})