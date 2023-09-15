from django.urls import path
from .views import *

urlpatterns = [
    path('api/',PersonAPIview.as_view()),
    path('api/details/<int:id>/',PersonDetails.as_view())
]
