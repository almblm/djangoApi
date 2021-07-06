from rest_framework import routers
from sample.views import SampleViewSet

router = routers.DefaultRouter()
router.register(r'sample',SampleViewSet)