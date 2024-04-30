from django.contrib import admin
from django.urls import path, include
from app.views import Home  # Import the Home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),  # Define URL pattern for the root URL
    path('app/', include('app.urls'))
]
