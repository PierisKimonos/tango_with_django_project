from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of shortcut function to make our lives easier.
    # Note that the first parameter is the tmeplate we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):

    context_dict = {}

    return render(request, 'rango/about.html', context=context_dict)