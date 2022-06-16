from django.contrib import admin

# Register your models here.

from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin): 
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('id', 'name', 'year_formed', 'genre') 

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'sold', 'band')

# Nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)