# myapi/urls.pyfrom django.urls import include, path
from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'company/customer/note', views.CustomerNoteViewSet)
router.register(r'company/customer', views.CustomerViewSet)
router.register(r'company', views.CompanyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('customer/', views.CustomersFilterList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]