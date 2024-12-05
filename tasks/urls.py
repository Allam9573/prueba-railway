from rest_framework import routers
from .views import TaskViewset

router = routers.DefaultRouter()

router.register('', TaskViewset, basename='tasks')
urlpatterns = router.urls