from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from profile_api.views import *

router = DefaultRouter()
router.register('hello-viewset', viewset=HelloViewSet, base_name='hello-viewset')
router.register('profile', viewset=UserProfileViewset)
router.register('login', viewset=LoginViewSet, base_name='login')
router.register('feed', viewset=UserProfileFeedViewSet, base_name='profile-feed')

urlpatterns = [
    url(r'^hello-view/', HelloApiView.as_view()),
    url(r'', include(router.urls))
]
