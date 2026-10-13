from django.urls import path, include 

from rest_framework.routers import DefaultRouter 

from .views import * 

router = DefaultRouter() 

router.register(r'cliente', ClienteViewSet, basename="cliente")
router.register(r'imovel', ImovelViewSet, basename="imovel")
router.register(r'fatura', FaturaViewSet, basename="fatura")

urlpatterns = [
    path('', include(router.urls))
]