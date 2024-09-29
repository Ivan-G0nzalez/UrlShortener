from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UrlViewSet  # Make sure this import is correct

router = DefaultRouter()
router.register(r'urls', UrlViewSet)  # Registers the ViewSet with all the standard CRUD URLs

urlpatterns = [
    path('', include(router.urls)),  # This should include all the URLs from the router
    path('shorten/<str:shortcode>/stats/', UrlViewSet.as_view({'get':'retrieve_stats'}), name='stats-details')
]