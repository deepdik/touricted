from rest_framework.generics import (
	ListAPIView,
	UpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
	RetrieveAPIView,
	ListCreateAPIView,
	RetrieveUpdateDestroyAPIView
	)
from rest_framework.views import APIView
from rest_framework.permissions import (
	IsAuthenticated,
	IsAdminUser,
	AllowAny,
	)

from tourist.models import (
	Category,
	Package,
	Hotel,
	ItineraryDays,
	Inclusion,
	Activity,
	Destination,
	HotelTest,
	HotelsForPackage,
	Image	
	)

from .serializers import (
	CategoryListSerializer,
	PackageListSerializer,
	CategoryDetailSerializer,
	PackageDetailSerializer,
	HotelListSerializer,
	InclusionDetailSerializer,
	ActivityDetailSerializer,
	DestinationDetailSerilizer,
	HotelListSerializer,
	HotelAddSerializer,
	HoteltestCreateSerializer,
	ImageUploadSerializer,
	ItineraryAddSerializer,
	PackageCreateSerializer,
	DestinationListSerializer	
	)


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from django_filters import rest_framework as filters
import django_filters


class CategoryListCreateAPIView(ListCreateAPIView):

	queryset = Category.objects.all()
	serializer_class = CategoryListSerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryDetailSerializer
	lookup_field = "id"

class InclusionListCreateAPIView(ListCreateAPIView):

	queryset = Inclusion.objects.all()
	serializer_class = InclusionDetailSerializer

class InclusionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Inclusion.objects.all()
	serializer_class = InclusionDetailSerializer
	lookup_field = "id"

class ActivityListCreateAPIView(ListCreateAPIView):

	queryset = Activity.objects.all()
	serializer_class = ActivityDetailSerializer

class ActivityRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Activity.objects.all()
	serializer_class = ActivityDetailSerializer
	lookup_field = "id"


class DestinationFilter(django_filters.FilterSet):	
	Best_time_for_travel = django_filters.RangeFilter(field_name='ActualPricePerPerson')
	

	class Meta:
		model = Destination
		fields = {'DestinationType','package'}

class DestinationListSerializer(APIView):
	queryset = Destination.objects.all()
	serializer_class = DestinationListSerializer
	filter_backends = (DjangoFilterBackend,)
	filterset_class = DestinationFilter

class testAPIView(APIView):
	def get(self,request):
		id =request.GET.get('id')
		print(id,'idddddddddd')
		return Response("successfully")

from rest_framework.decorators import api_view
@api_view(['get'])
def xyz(self,request):
	id =request.GET.get('id')
	print(id,'idddddddddd')
	return Response("successfully")

class DestinationListCreateAPIView(ListCreateAPIView):

	queryset = Destination.objects.all()
	serializer_class = DestinationDetailSerilizer
	filter_backends = (DjangoFilterBackend,)
	filterset_fields =('DestinationType',) 

class DestinationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Destination.objects.all()
	serializer_class = DestinationDetailSerilizer
	lookup_field = "id"

class HotelListCreateAPIView(ListAPIView):
	queryset = Hotel.objects.all()
	
class HotelCreateAPIView(CreateAPIView):


	def post(self, request, format=None):
		serializer = HoteltestCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)

#Completed
class HotelAddAPIView(APIView):
	def post(self, request, format=None):
		serializer = HotelAddSerializer(data=request.data)		
		if serializer.is_valid():		
			serializer.save()			
			return Response(request.data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#completed
class ItineraryAddAPIView(APIView):
	def post(self, request, format=None):
		serializer = ItineraryAddSerializer(data=request.data)		
		if serializer.is_valid():		
			serializer.save()			
			return Response(request.data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#package filter completed
class PackageFilter(django_filters.FilterSet):
	
	price_per_persion = django_filters.RangeFilter(field_name='ActualPricePerPerson')
	package_days = django_filters.RangeFilter(field_name='PackageDays')
	# hotel__stars = django_filters.NumberFilter(field_name=hotel_package)
	class Meta:
		model = Package
		fields = {'category','package_days','price_per_persion','Destination__DestinationType','activity','inclusion',
			'Destination'}

class PackageListAPIView(ListAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageListSerializer
	filter_backends = (DjangoFilterBackend,)
	filterset_class = PackageFilter
	# filterset_fields = ('category','OfferedPricePerPerson','PackageDays','Destination',
	# 	'activity','Destination__DestinationType','inclusion')
	# permissions_classes = (IsUser,)

class PackageCreateAPIView(CreateAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageCreateSerializer
	# permissions_classes = (IsAuthenticated,IsAdminUser)

class PackageUpdateAPIView(UpdateAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageCreateSerializer
	lookup_field = "id"
	# permissions_classes = (IsAuthenticated,IsAdminUser)

class PackageDeleteAPIView(DestroyAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageCreateSerializer
	lookup_field = "id"
	# permissions_classes = (IsAuthenticated,IsAdminUser)

class PackageDetailAPIView(RetrieveAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageDetailSerializer
	lookup_field = "id"
	# permissions_classes = (IsAuthenticated,IsAdminUser)

class PackageListCategoryAPIView(ListAPIView):	
	serializer_class = PackageListSerializer
	def get_queryset(self):
		catId = self.kwargs['catId']
		obj = Package.objects.filter(category_id =catId)
		#to get att
		print(obj.values_list('id', flat=True).order_by('id'))
		return Package.objects.filter(category_id =catId)

# class DestinationListAPIView(APIView):
	

# class RecentlyViewedListAPIView(ListAPIView):
# 	serializer_class = PackageListSerializer
# 	def get_queryset(self):
# 		package_id = self.kwargs['id']
# 		return Package.objects.filter(id =package_id)

class ImageUploadAPIView(CreateAPIView):	
	serializer_class = ImageUploadSerializer



		


	





