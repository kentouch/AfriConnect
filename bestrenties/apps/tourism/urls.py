"""from django.urls import path
from . import views

app_name = 'tourism'

urlpatterns = [
    path('', views.index, name='tourism_index'),

]"""

# tourism/urls.py
# tourism/urls.py

from django.urls import path
from . import views

app_name = 'tourism'

urlpatterns = [
    path('', views.tourism_view, name='tourism'),
    path('submit-request/', views.send_test_tour_email, name='submit_tour_request'),
]
    
    