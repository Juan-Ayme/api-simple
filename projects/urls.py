from rest_framework import routers
from .api import ProductorViewSert

router = routers.DefaultRouter()

router.register('api/productor', ProductorViewSert, 'productor')

urlpatterns = router.urls
