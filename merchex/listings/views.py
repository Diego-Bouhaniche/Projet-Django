from re import L
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

from listings.forms import BandForm, ContactUsForm, ListingForm
from listings.models import Band, Listing

# Create your views here.

## BAND ##
def band_list(request):
    bands = Band.objects.all()
    return render(request, 
        'listings/groupes/band_list.html',
        {'bands': bands}
    )
    
def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/groupes/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)

        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
        else:
            messages.warning(request, 'POST : Form is invalid !')
    else:
        form = BandForm()

    return render(request,
            'listings/groupes/band_create.html',
            {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)  # on pré-remplir le formulaire avec un groupe existant
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
        else:
            messages.warning(request, 'POST : Form is invalid !')
            
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/groupes/band_update.html',
                {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    
    return render(request,
                    'listings/groupes/band_delete.html',
                    {'band': band})

## LISTING ##
def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 
        'listings/annonces/listing_list.html',
        {'listings': listings}
    )

def listing_detail(request, id):
  listings = Listing.objects.get(id=id)
  return render(request,
          'listings/annonces/listing_detail.html',
          {'listing': listings})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)
        else:
            messages.warning(request, 'POST : Form is invalid !')

    else:
        form = ListingForm()

    return render(request,
            'listings/annonces/listing_create.html',
            {'form': form})

def listing_update(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)  # on pré-remplir le formulaire avec un groupe existant
        
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('listing-detail', listing.id)
        else:
            messages.warning(request, 'POST : Form is invalid !')

    else:
        form = ListingForm(instance=listing)

    return render(request,
                'listings/annonces/listing_update.html',
                {'form': form})

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        listing.delete()
        # rediriger vers la liste des groupes
        return redirect('listing-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/annonces/listing_delete.html',
                    {'listing': listing})

## AUTRE ##
def about(request):
    return render(request,
            'listings/autres/about.html')
            
def contact(request):   
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
        else:
            messages.warning(request, 'POST : Form is invalid !')

        return redirect('email-sent')  # ajoutez cette instruction de retour
        
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
            'listings/autres/contact.html',
            {'form': form})

def email_sent(request):
  return render(request,
          'listings/autres/email_sent.html')