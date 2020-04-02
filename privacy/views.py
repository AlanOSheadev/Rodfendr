from django.shortcuts import render


# Create your views here.
def privacy(request):
    """ A view that displays a privacy page """
    return render(request, "privacy.html")
