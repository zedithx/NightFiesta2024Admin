from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("", views.AccountView, basename="accountview")
urlpatterns = router.urls