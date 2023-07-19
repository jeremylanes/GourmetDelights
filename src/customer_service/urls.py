from django.urls import path

from customer_service.views import message

app_name = "customer-service"
urlpatterns = [
    path('message/', message, name='message'),
]
