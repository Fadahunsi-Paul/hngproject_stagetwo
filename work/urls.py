from django.urls import path
from .views import *

urlpatterns = [
    path('api/',PersonAPIview.as_view()),
    path('details/<int:id>/',PersonDetails.as_view())
]
