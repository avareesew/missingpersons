from django.urls import path 
from .views import indexPageView, statisticsPageView

urlpatterns = [
    path('', indexPageView, name= "index"),
    path('statistics/', statisticsPageView, name='statistics'),
]
