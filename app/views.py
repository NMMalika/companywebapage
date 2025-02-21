from django.shortcuts import render

# Create your views here.
def index(request):
    products =[
        {"name":"laptop", "price": 1000},
        {"name":"mobile", "price": 500},
        {"name":"tablet", "price": 300},
        {"name":"smartwatch", "price": 200},
        {"name":"headphone", "price": 100},
    ]
    context={
        "products": products,
    }
    return render(request, "index.html", context)
