from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
# Register viewsets here when available, e.g.:
# router.register(r'users', views.UserViewSet)
# router.register(r'teams', views.TeamViewSet)
# router.register(r'activities', views.ActivityViewSet)
# router.register(r'workouts', views.WorkoutViewSet)
# router.register(r'leaderboard', views.LeaderboardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
