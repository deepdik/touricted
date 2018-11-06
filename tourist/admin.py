from django.contrib import admin
from tourist.models import (Package,Category,Hotel,HotelImage,
	Itinerary,ItineraryDays,Activity,Image,Inclusion,HotelImage,Destination,HotelsForPackage,Packageimages)

class HotelsForPackageInline(admin.TabularInline):
    model = HotelsForPackage
    extra = 1

class PackageimagesInline(admin.TabularInline):
    model = Packageimages
    extra = 1


class PackageAdmin(admin.ModelAdmin):
	list_display = ('PackageName','Destination',)
	list_filter = ('PackageName','Destination')
	inlines = [ HotelsForPackageInline, PackageimagesInline,]
	# list_editable = ('category','pricingTabName')
	# search_fields = ('PackageName')
	
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','timestamp')
	# search_fields = ('name')


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 2

class HotelAdmin(admin.ModelAdmin):
    inlines = [ HotelImageInline, ]



class ItineraryDaysInline(admin.TabularInline):
    model = ItineraryDays
    extra = 1

class ItineraryAdmin(admin.ModelAdmin):
    inlines = [ ItineraryDaysInline]



admin.site.register(Itinerary, ItineraryAdmin)

admin.site.register(Activity)

admin.site.register(Inclusion)
admin.site.register(Image)
# admin.site.register(HotelImage)
# admin.site.register(ItineraryDays)
admin.site.register(Destination)


admin.site.register(Hotel, HotelAdmin)


admin.site.register(Package,PackageAdmin)
admin.site.register(Category,CategoryAdmin)

