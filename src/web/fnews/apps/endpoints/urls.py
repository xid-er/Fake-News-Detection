from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet, MLAlgorithmViewSet, MLAlgorithmStatusViewSet, MLRequestViewSet, PredictView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

app_name = "endpoints"

urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
    re_path(
        r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
    ),
]