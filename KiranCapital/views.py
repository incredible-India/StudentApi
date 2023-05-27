from django.shortcuts import render


#this is the default home page ('' default route)
def index(request):

    return render(request, 'index.html',status=200)