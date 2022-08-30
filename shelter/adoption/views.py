from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
doggos = [
    {'id': 1, "name": "tom", "breed": "Cockapoo", "owner": "No one"},
    {'id': 2, "name": "harry", "breed": "Collie", "owner": "No one"},
    {'id': 3, "name": "alan", "breed": "Shitzu", "owner": "No one"},
    {'id': 4, "name": "flo", "breed": "Beagle", "owner": "No one"},
    {'id': 5, "name": "ali", "breed": "Bard", "owner": "No one"}
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("<h1>Read all about us here</h1>")

def dogs(request):
    # return HttpResponse(
    #     "<h1> These are all the dogs </h1>"
    #     f"<p> We have {len(doggos)} in our shelter! </p>"
    # )
    data = { 'doggos' : doggos }
    return render(request, 'dogs.html', data)

def show(request, id):
    dog = list(filter(lambda doggo: doggo['id'] == id, doggos))
    return HttpResponse(
        f"<h1> This is a page for dog number {id} </h1>"
        f"<p> Their name is {dog[0]['name']}. </p>"
    )