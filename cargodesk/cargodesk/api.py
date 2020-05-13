from rest_framework import routers
from cargos import api_views as cargos_views


router = routers.DefaultRouter()
router.register(r'shipments', cargos_views.ShipmentViewSet)
router.register(r'todos', cargos_views.TodoViewSet)
