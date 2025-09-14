from django.contrib import admin
from django.urls import path, include
from server import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wines', viewset=views.WineViewSet, basename='wine')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
