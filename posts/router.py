from rest_framework import routers

from profiles.views import ProfilesViewSet, ProfileStatusViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)
