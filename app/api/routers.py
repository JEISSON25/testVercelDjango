from rest_framework.routers import DefaultRouter
from ..state.views import *
from ..file.views import *

router = DefaultRouter()

router.register(r'state', StateViewset, basename='state')
router.register(r'file', FileViewset, basename='file')


urlpatterns = router.urls