from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from banks import views as banks_views
from programs import views as programs_views
from transactions import views as transactions_views

router = routers.DefaultRouter()
router.register(r'banks', banks_views.BankViewSet, basename="banks")
router.register(r'programs', programs_views.ProgramViewSet, basename="programs")
router.register(r'transactions', transactions_views.TransactionViewSet, basename="transactions")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
