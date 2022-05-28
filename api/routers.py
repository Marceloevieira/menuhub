from rest_framework import routers
from api.viewsets import GroupViewSet, MenuItemViewSet, RestaurantViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r"v1/restaurants", RestaurantViewSet)
router.register(r"v1/menu-itens", MenuItemViewSet)
router.register(r"v1/users", UserViewSet)
router.register(r"v1/groups", GroupViewSet)
