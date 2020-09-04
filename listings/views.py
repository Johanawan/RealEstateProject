from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, area_choices

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
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    context = {
        'area_choices': area_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'listings/search.html', context)