from rest_framework import routers
from .views import CarView

router = routers.DefaultRouter()
router.register('api/cars', CarView, 'car')

urlpatterns = router.urls

