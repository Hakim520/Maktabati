from django.urls import path,include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from . import views

router = DefaultRouter()


router.register(r"genre",views.GenreViewSet)
router.register(r"books",views.BookViewSet)

router.register(r'accounts', views.AccountViewSet)
router.register(r'cart_items', views.CartItemsViewSet, basename='cart-items')
router.register(r'facture_items', views.FactureItemsViewSet, basename='facture-items')



urlpatterns = [
    path("",include(router.urls)),
    path("schema/",SpectacularAPIView.as_view(), name ="schema"),
    path("schema/docs/",SpectacularSwaggerView.as_view(url_name = "schema"))
]