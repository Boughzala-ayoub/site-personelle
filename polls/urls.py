from django.urls import path
from .views import detail, index, cv, contact

app_name = 'polls'


urlpatterns = [
    path('', index, name='index'),
    path('resume/', detail, name='detail'),
    path('cv/', cv, name='cv'),
    path('contact/', contact, name='contact'),
]
