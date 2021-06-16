from django.shortcuts import render
from .models import Destination
# Create your views here.
 
dest1= Destination()
dest1.name='Warangal'
dest1.desc='A Historical Place'
dest1.price='50000'
dest1.img='destination_4.jpg'
dest1.offer=False

dest2 =Destination()
dest2.name='Hyderabad'
dest2.desc='A Deccan city'
dest2.price='60000'
dest2.img='destination_1.jpg'
dest2.offer=True

dest3 =Destination()
dest3.name='Pune'
dest3.desc='Monsoon destination'
dest3.price='70000'
dest3.img='destination_3.jpg'
dest3.offer=False

dests=[dest1,dest2,dest3]

def index(request):
    return render(request,'index.html', {'dests': dests })
