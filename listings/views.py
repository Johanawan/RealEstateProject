from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

# Create your views here.


def index(request):

    # Lists listings by date order and displays published listings only.

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # Tells paginator we want to paginate listings with 6 listings per page.
    paginator = Paginator(listings, 6)

    # Get request for the pages
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    
    context = {
        'listings': page_listings,

    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')