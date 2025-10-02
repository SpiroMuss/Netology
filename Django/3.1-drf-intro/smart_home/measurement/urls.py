from django.urls import path
from .views import SensorRetrieveUpdateAPIView, SensorListCreateView, MeasurementListCreateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты

    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<pk>', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementListCreateView.as_view())
]
