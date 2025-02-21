from django.shortcuts import render

# Create your views here.
def index(request):
   

    context={
        "names": ["John", "Jane", "Doe"],
    
        "can_vote": True,
    }
    return render(request, "index.html", context)
