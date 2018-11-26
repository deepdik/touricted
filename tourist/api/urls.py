from django.conf.urls import url
from .views import (
# CategoryListAPIView,
# CategoryCreateAPIView,
# CategoryUpdateAPIView,
# CategoryDeleteAPIView,
CategoryListCreateAPIView,
CategoryRetrieveUpdateDestroyAPIView,
PackageListAPIView,
PackageCreateAPIView,
PackageUpdateAPIView,
PackageDeleteAPIView,
PackageDetailAPIView,
PackageListCategoryAPIView,

InclusionListCreateAPIView,
InclusionRetrieveUpdateDestroyAPIView,
ActivityListCreateAPIView,
ActivityRetrieveUpdateDestroyAPIView,
DestinationListCreateAPIView,
DestinationRetrieveUpdateDestroyAPIView,
HotelListCreateAPIView,
HotelCreateAPIView,
# HotelTestCreateAPIView,
HotelAddAPIView,
# RecentlyViewedListAPIView
ImageUploadAPIView,
ItineraryAddAPIView,
testAPIView

)


urlpatterns = [

  url(r'^categories/$',CategoryListCreateAPIView.as_view(),name="CategoriesCreateDestination"),
  url(r'^edit-delete-categories/(?P<id>\d+)/$',CategoryRetrieveUpdateDestroyAPIView.as_view(),name="updatedeleteCategories"),

  url(r'^packages/$',PackageListAPIView.as_view(),name="listPackage"),
  url(r'^addpackage/$',PackageCreateAPIView.as_view(),name="addPackage"),
  url(r'^editpackage/(?P<id>\d+)/$',PackageUpdateAPIView.as_view(),name="updatePackage"),
  url(r'^deletepackage/(?P<id>\d+)/$',PackageDeleteAPIView.as_view(),name="deletePackage"),

  url(r'^package/detail/(?P<id>\d+)/$',PackageDetailAPIView.as_view(),name="detailPackage"),
  url(r'^packages/(?P<catId>\d+)/$',PackageListCategoryAPIView.as_view(),name="packageCatList"),


  url(r'^inclusions/$',InclusionListCreateAPIView.as_view(),name="listCreateInclusion"),
  url(r'^edit-delete-inclusions/(?P<id>\d+)/$',InclusionRetrieveUpdateDestroyAPIView.as_view(),name="updatedeleteinclusion"),

  url(r'^activities/$',ActivityListCreateAPIView.as_view(),name="ActivityCreateActivities"),
  url(r'^edit-delete-activity/(?P<id>\d+)/$',ActivityRetrieveUpdateDestroyAPIView.as_view(),name="updateDeleteActivity"),

  url(r'^destination/$',DestinationListCreateAPIView.as_view(),name="listCreateDestination"),
  url(r'^edit-delete-destination/(?P<id>\d+)/$',DestinationRetrieveUpdateDestroyAPIView.as_view(),name="updatedeleteDestination"),

  # url(r'^recently_viewed/?fields=id$',RecentlyViewedListAPIView.as_view(),name="recentlyViewedPackage"),

  url(r'^hotel1/$',HotelListCreateAPIView.as_view(),name="listCreateHotel"),
  # url(r'^edit-delete-hotel/(?P<id>\d+)/$',DestinationRetrieveUpdateDestroyAPIView.as_view(),name="updatedeleteDestination"),
  url(r'^add-hotel/$',HotelCreateAPIView.as_view(),name="updDestination"),
  # url(r'^add-hotels/$',HotelTestCreateAPIView.as_view(),name="updatesDestination"),

  url(r'^image-upload/$',ImageUploadAPIView.as_view(),name="ImageUpload"),

  url(r'^hotels/$',HotelAddAPIView.as_view(),name="CreateHotel"),


  url(r'^itinerary/$',ItineraryAddAPIView.as_view(),name="CreateHotel"),
  # url(r'^test$' ,views.xyz, name="api"),


]
