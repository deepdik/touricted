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
	ItineraryAddSerializer	
	)



from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
# class CategoryListAPIView(ListAPIView):
# 	queryset = Category.objects.all()
# 	serializer_class = CategoryListSerializer
# 	# permissions_classes = (IsUser,)

# class CategoryCreateAPIView(CreateAPIView):
# 	queryset = Category.objects.all()
# 	serializer_class = CategoryDetailSerializer
# 	# permissions_classes = (IsAuthenticated,IsAdminUser)

# class CategoryUpdateAPIView(UpdateAPIView):
# 	queryset = Category.objects.all()
# 	serializer_class = CategoryDetailSerializer
# 	lookup_field = "id"
# 	# permissions_classes = (IsAuthenticated,IsAdminUser)

# class CategoryDeleteAPIView(DestroyAPIView):
# 	queryset = Category.objects.all()
# 	serializer_class = CategoryDetailSerializer
# 	lookup_field = "id"
# 	# permissions_classes = (IsAuthenticated,IsAdminUser)


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


class DestinationListCreateAPIView(ListCreateAPIView):

	queryset = Destination.objects.all()
	serializer_class = DestinationDetailSerilizer

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








class PackageListAPIView(ListAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageListSerializer
	# permissions_classes = (IsUser,)

class PackageCreateAPIView(CreateAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageDetailSerializer
	# permissions_classes = (IsAuthenticated,IsAdminUser)

class PackageUpdateAPIView(UpdateAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageDetailSerializer
	lookup_field = "id"
	# permissions_classes = (IsAuthenticated,IsAdminUser)

class PackageDeleteAPIView(DestroyAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageDetailSerializer
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
		return Package.objects.filter(category_id =catId)


# class RecentlyViewedListAPIView(ListAPIView):
# 	serializer_class = PackageListSerializer
# 	def get_queryset(self):
# 		package_id = self.kwargs['id']
# 		return Package.objects.filter(id =package_id)

class ImageUploadAPIView(CreateAPIView):	
	serializer_class = ImageUploadSerializer



		


	





