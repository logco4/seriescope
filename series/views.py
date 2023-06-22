from django.http import HttpResponse


def index(request):
    return HttpResponse("Dude, you ran out of eggs. Do you want to buy an 80 pack of eggs?")
