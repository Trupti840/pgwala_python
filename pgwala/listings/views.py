from django.shortcuts import render
from .models import PGListing

def listing_list(request):
    query = request.GET.get('q')
    listings = PGListing.objects.all()

    if query:
        listings = listings.filter(location__icontains=query)

    return render(request, 'listings/listing_list.html', {'listings': listings})
