from rest_framework.routers import DefaultRouter

from applications.core.views.reservations_view import ReservationsView

router = DefaultRouter()
router.register(r'reservations', ReservationsView, basename='reservations')
urlpatterns = router.urls
