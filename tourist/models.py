from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

TYPE = (('domestic', 'Domestic'), ('international', 'International'))
MONTHS = (('january','JAN'),('february','FEB'),('march','MAR'),('april','APR'),('may','MAY'),
	('june','JUN'),('july','JUL'),('august','AUG'),('september','SEP'))

def upload_location(instance, filename):
	return 'Package/%s-%s/%s' % (instance.PackageName, instance.id, filename)

def itenery_img_location(instance,filename):
	return 'Itinerary/%s-%s/%s' % (instance.Day, instance.id, filename)

class Category(models.Model):

	name = models.CharField(max_length=120, unique=True)
	CatImg = models.FileField(upload_to='CatImg/',default='CatImg/None/default.svg')
	timestamp = models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Categories"

class Inclusion(models.Model):
	name = models.CharField(max_length=30,unique=True)
	InclImg = models.ImageField(upload_to='InclusionImg/',
						   default='InclusionImg/None/default.png',
						   )
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Inclusions"

class Activity(models.Model):
	name = models.CharField(max_length=30,unique=True)
	ActImg = models.ImageField(upload_to='ActivitieImg/',
						   default='ActivitieImg/None/default.png',
						   )
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Activities"


class Destination(models.Model):
	DestinationType = models.CharField(max_length=120, choices=TYPE)
	name = models.CharField(max_length =120,unique=True)
	image = models.ImageField()
	Best_time_for_travel_from = models.CharField(max_length=120, choices=MONTHS)
	Best_time_for_travel_to = models.CharField(max_length=120, choices=MONTHS)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	def __int__(self):
		return self.Day

	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Destinations"



class Hotel(models.Model):	
	name = models.CharField(max_length=150)
	facilities = models.TextField(null=True)
	address = models.CharField(max_length=300)
	About = models.TextField()
	Stars = models.IntegerField(
		default=0,
		validators=[
			MaxValueValidator(5),
			MinValueValidator(0)
		]
	 )
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
	class Meta:
		# ordering = ('timestamp')
		verbose_name_plural = "Hotels"

class HotelTest(models.Model):
	# hotel =  models.ForeignKey(Hotel, related_name = 'Hotel_test')
	# facility = models.CharField(max_length = 120,default="facility")
	image = models.ImageField()



class HotelImage(models.Model):
	hotel = models.ForeignKey(Hotel, related_name = 'Hotel_images')
	image = models.ImageField(null=True,blank=True)
	images = models.URLField(default="/image")
	# caption = models.CharField(max_length = 120,default = 'name of Itenery')


class Itinerary(models.Model):
	name = models.CharField(max_length = 120)	# def __str__(self):

	def __str__(self):
		return self.name
	class Meta:
		# ordering = ('timestamp')
		verbose_name_plural = "Itinerarys"
		
class ItineraryDays(models.Model):
	
	itinerary = models.ForeignKey(Itinerary, related_name = 'ItineraryDays_days')
	Cities = models.CharField(max_length = 120,default = 'cities')
	Day =  models.PositiveIntegerField()
	Inclusion = models.ManyToManyField(Inclusion)

	Title = models.CharField(max_length = 120,default = 'title')
	About = models.TextField(default = 'About')
	Labels = models.TextField(blank = True, null = True)
	Image_One = models.ImageField(upload_to = itenery_img_location,blank=True, null=True)
	Image_Two = models.ImageField(upload_to = itenery_img_location,blank=True, null=True)
	Image_Three = models.ImageField(upload_to = itenery_img_location,blank=True, null=True)

	def __int__(self):
		return self.Day


	class Meta:
		ordering = ('id',)
		verbose_name_plural = "ItineraryDays"

class Package(models.Model):
	PackageName = models.CharField(max_length=120, unique=True)
	Destination  = models.ForeignKey(Destination)
	PackageDays = models.PositiveSmallIntegerField(default=1)
	PackageNights = models.PositiveSmallIntegerField(default=1)
	category = models.ForeignKey(Category)
	activity = models.ManyToManyField(Activity)
	inclusion = models.ManyToManyField(Inclusion)	

	# cities = models.CharField(max_length=120)
	Overview = models.TextField(default='overview of package')	
	Highlights = models.TextField(blank=True,null=True)
	Itinerary = models.OneToOneField(Itinerary, on_delete=models.PROTECT)

	Inclusion_text =  models.TextField()
	Exclusion_text= models.TextField()
	ActualPricePerPerson = models.PositiveIntegerField(default = 1)
	OfferedPricePerPerson = models.PositiveIntegerField(default = 1)
	DepartureCity = models.CharField(max_length = 120)

	BannerImage = models.ImageField(upload_to = upload_location,
									default ='Package/None/default.png',
									)       
	# NightOneLessThanDay	=  models.PositiveIntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.PackageName

	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Packages"



class Packageimages(models.Model):
	package = models.ForeignKey(Package, related_name = 'Package_images')
	image = models.ImageField()
	caption = models.CharField(max_length = 120,default = 'image Captions')



class HotelsForPackage(models.Model):
	day = models.CharField(max_length = 20,default = '1-2')
	package = models.ForeignKey(Package, default=1,related_name = 'hotel_package')
	hotel = models.ForeignKey(Hotel, related_name = 'hotel_name')

	class Meta:
		verbose_name_plural = "Hotels For Package"


class Image(models.Model):
	image = models.ImageField()
	caption = models.CharField(max_length = 50,null=True,blank=True)

	class Meta:
		verbose_name_plural = "Images"

