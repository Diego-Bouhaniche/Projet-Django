from django.http import HttpResponse
from django.shortcuts import render

from listings.forms import ContactUsForm
from listings.models import Band, Listing

# Create your views here.

## BAND ##
def band_list(request):
    bands = Band.objects.all()
    return render(request, 
        'listings/band_list.html',
        {'bands': bands}
    )
    
def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit


## LISTING ##
def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 
        'listings/listing_list.html',
        {'listings': listings}
    )

def listing_detail(request, id):
  listings = Listing.objects.get(id=id)
  return render(request,
          'listings/listing_detail.html',
          {'listing': listings})


## AUTRE ##
def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):   
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    # ajout d’un nouveau formulaire ici
    form = ContactUsForm()

    return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit

          
