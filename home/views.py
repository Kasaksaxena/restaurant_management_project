from django.shortcuts import render
from .models import RestaurantInfo

# Create your views here.
def homepage(request):
    restaurant=RestaurantInfo.objects.first()
    context={
        'restaurant_name':restaurant.name if restaurant else "Our Restaurant",
        'phone_number':settings.RESTAURANT_PHONE_NUMBER
    }
    return render(request,'home/index.html',context)
