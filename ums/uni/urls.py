# books/urls.py
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ResultViewSet

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")
router.register(r"results", ResultViewSet, basename='result')

urlpatterns = router.urls