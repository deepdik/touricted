from tourist.models import (
	Category,
	Package,
	Hotel,
	HotelImage,
	Itinerary,
	ItineraryDays,
	HotelsForPackage,
	Activity,
	Inclusion,
	Packageimages,
	Destination,
	HotelTest,
	Image

	)
from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,
	DateTimeField,  
	ValidationError,

	)
from drf_extra_fields.fields import Base64ImageField


class CategoryListSerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = [
			'id',
			'name',                     
			'CatImg',
		]

class CategoryDetailSerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = [
			'name',         
			'CatImg'
		]

class ActivityDetailSerializer(ModelSerializer):
	class Meta:
		model = Activity
		fields = ['name','ActImg']

class InclusionDetailSerializer(ModelSerializer):
	class Meta:
		model = Inclusion
		fields = ['name','InclImg']

class PackageimagesListSerilizer(ModelSerializer):
	class Meta:
		model = Packageimages
		fields = ['image','caption']

class DestinationDetailSerilizer(ModelSerializer):
	class Meta:
		model  = Destination
		fields = '__all__'

class HotelImageListSerializer(ModelSerializer):
	class Meta:
		model = HotelImage
		fields = ['image','caption']




class HotelListSerializer(ModelSerializer):
	images = SerializerMethodField()
	facilities = SerializerMethodField()

	def get_images(self,instance):

		hotel = HotelImage.objects.filter(hotel = instance.id)
		data = HotelImageListSerializer(hotel,many=True).data
		return data

	def get_facilities(self,instance):
		fac_str  =   instance.facilities
		fac_list= fac_str.split(",")        
		return fac_list

	class Meta:
		model = Hotel
		fields = ['id','name','facilities','address','About','Stars','images']



class HoteltestCreateSerializer(ModelSerializer):
	
	# image =Base64ImageField()   
	

	class Meta:
		model=HotelTest
		fields= ['image']

	def create(self, validated_data):
		image=validated_data.pop('image')
	  
		return HotelTest.objects.create(image=image)

class HotelAddSerializer(ModelSerializer):
	facility = HoteltestCreateSerializer(many=True)


	class Meta:
		model = Hotel
		fields  =['name','address','About','Stars','facility']


	def create(self, validated_data):
		facilities_data = validated_data.pop('facility')	
		hotel = Hotel.objects.create(**validated_data)
		for facility_data in facilities_data:
			HotelTest.objects.create(hotel=hotel, **facility_data)			
		return hotel


#   def create(self,validate_data):
# #         shopSlug = validate_data['shopSlug']
# #         shop = validate_data['shopSlug']
# #         content = validate_data["content"]
# #         user = self.context['request'].user
# #         print ("hello")
# #         print (self.context['request'].COOKIES['token'])
# #         print(self.context['request'].META['REMOTE_ADDR'])
# #         return Feedback.objects.create(
# #             user = user,
# #             shop = shop,
# #             content=content
# #             )


class HotelsForPackageSerializer(ModelSerializer):
	hotel = HotelListSerializer()
	class Meta:
		model = HotelsForPackage
		fields = ['day','hotel']

class ItineraryDayListSerializer(ModelSerializer):
	Inclusion = InclusionDetailSerializer(many=True)
	
	class Meta:
		model = ItineraryDays
		fields = [

			'Day',
			'Title',
			'Cities',
			'About',
			'Labels',
			'Inclusion',        
			'Image_One',
			'Image_Two',
			'Image_Three'
		]

	
class ItineraryListSerializer(ModelSerializer):
	itinerary = SerializerMethodField()
	
	def get_itinerary(self,instance):
		itinerary = ItineraryDays.objects.filter(itinerary = instance.id)
		data = ItineraryDayListSerializer(itinerary,many=True).data
		return data

	class Meta:
		model = Itinerary
		fields = [          
			'itinerary',                        

		]

class PackageDetailSerializer(ModelSerializer):
	activity = ActivityDetailSerializer(many=True)
	inclusion = InclusionDetailSerializer(many=True)
	offer = SerializerMethodField()
	offer = SerializerMethodField()
	category = CategoryDetailSerializer()
	IncludeHotel = SerializerMethodField()
	Itinerary = SerializerMethodField()
	Inclusion_text = SerializerMethodField()
	Exclusion_text = SerializerMethodField()
	Packageimages = SerializerMethodField()
	Destination = DestinationDetailSerilizer()
	cities  =SerializerMethodField()

	def get_offer(self,instance):
		ActualPrice  =   instance.ActualPricePerPerson
		OfferedPrice  =instance.OfferedPricePerPerson
		Per_offer = str((ActualPrice - OfferedPrice)*100 // ActualPrice) +'%'       
		return Per_offer

	def get_IncludeHotel(self,instance):        
		hotel = HotelsForPackage.objects.filter(package = instance.id)
		data = HotelsForPackageSerializer(hotel,many=True).data
		return data

	def get_Itinerary(self,instance):
		Itinerary = ItineraryDays.objects.filter(itinerary=instance.Itinerary)
		data = ItineraryDayListSerializer(Itinerary,many=True).data
		return data

	def get_Inclusion_text(self,instance):
		Incls_str = instance.Inclusion_text
		Incls_list= Incls_str.split(",")
		
		return Incls_list

	def get_Exclusion_text(self,instance):
		Excls_str = instance.Exclusion_text
		Excls_list= Excls_str.split(",")        
		return Excls_list

	def get_Packageimages(self,instance):
		hotel = Packageimages.objects.filter(package = instance.id)
		data = HotelImageListSerializer(hotel,many=True).data
		return data

	def get_cities(self,instance):
		Itinerary = ItineraryDays.objects.filter(itinerary=instance.Itinerary)
		data = ItineraryDayListSerializer(Itinerary,many=True).data		
		cities = []
		for i in range(len(data)):
			cities.append(data[i]['Cities'])
		return cities

	class Meta:
		model = Package
		fields = [
			'id',           
			'category',
			'activity',
			'inclusion',
			'Itinerary',
			'PackageName',
			'cities',
			'Overview',
			'Highlights',
			'Destination',          
			'PackageDays',
			'PackageNights',        
			'Inclusion_text',
			'Exclusion_text',
			'ActualPricePerPerson',
			'OfferedPricePerPerson',
			'offer',
			'DepartureCity',            
			# 'NightOneLessThanDay',
			'IncludeHotel',
			'BannerImage',
			'Packageimages'
		]

class PackageListSerializer(ModelSerializer):
	offer = SerializerMethodField()
	category = CategoryDetailSerializer()
	inclusion = InclusionDetailSerializer(many=True)
	Destination = DestinationDetailSerilizer()
	cities  =SerializerMethodField()
	
	def get_offer(self,instance):
		ActualPrice  =   instance.ActualPricePerPerson
		OfferedPrice  =instance.OfferedPricePerPerson
		Per_offer = str((ActualPrice - OfferedPrice)*100 // ActualPrice) +'%'       
		return Per_offer

	def get_cities(self,instance):
		Itinerary = ItineraryDays.objects.filter(itinerary=instance.Itinerary)
		data = ItineraryDayListSerializer(Itinerary,many=True).data		
		cities = []
		for i in range(len(data)):
			cities.append(data[i]['Cities'])
		return cities
		
	class Meta:
		model = Package
		fields = [
			'id',           
			'category',
			'cities',
			'PackageName',
			'Destination',  
			'inclusion',
			'Destination',
			'PackageDays',
			'PackageNights',
			'ActualPricePerPerson',
			'OfferedPricePerPerson',
			'offer',
			'BannerImage',          
		]

class ImageUploadSerializer(ModelSerializer):

	class Meta:
		model = Image
		fields = [
			'image'

		]









