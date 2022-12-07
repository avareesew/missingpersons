from django.urls import path 
from .views import indexPageView, statisticsPageView, bePresentPageView, resourcesPageView

urlpatterns = [
    path('', indexPageView, name= "index"),
    path('statistics/', statisticsPageView, name='statistics'),
    path('bepresent/', bePresentPageView, name='bepresent'),
    path('resources/', resourcesPageView, name='resources'),
    
]
