"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.http import JsonResponse, HttpResponse
# Landing page view for root URL
def landing_page(request):
    return HttpResponse("""
        <html>
        <head><title>Octofit Tracker API</title></head>
        <body>
            <h1>Welcome to Octofit Tracker API</h1>
            <p>Use the <code>/api/</code> endpoints to access the REST API.</p>
            <ul>
                <li><a href='/api/url/'>API URL Info</a></li>
                <li><a href='/api/activities/'>Activities Endpoint</a></li>
            </ul>
        </body>
        </html>
    """)
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')

# Helper endpoint to return the API root URL using $CODESPACE_NAME
def api_url_info(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    api_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    return JsonResponse({'api_url': api_url})

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('admin/', admin.site.urls),
    path('api/url/', api_url_info, name='api-url-info'),
    path('api/', views.api_root, name='api-root'),
    path('api/', include(router.urls)),
]
