from django.urls import path

from django.contrib import admin
from django.urls import path

from measurement.views import AddListMeasurementView, AddListSensorView, ListSensorDetailView
from measurement.views import RetrieveUpdateDestroyMeasurementView, RetrieveUpdateDestroySensorView

urlpatterns = [
    path('sensor/', AddListSensorView.as_view()),
    path('changesensor/<pk>/', RetrieveUpdateDestroySensorView.as_view()),
    path('measurement/', AddListMeasurementView.as_view()),
    path('changemeasurement/<pk>/', RetrieveUpdateDestroyMeasurementView.as_view()),
    path('sensordetail/', ListSensorDetailView.as_view()),
]
