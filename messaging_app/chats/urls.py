from django.urls import path, include
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet

# Router
router = routers.DefaultRouter()
router.register(r"conversations", ConversationViewSet, basename="conversation")
router.register(r"messages", MessageViewSet, basename="message")

# Nested Router
nested_router = routers.NestedDefaultRouter(
    router, r"conversations", lookup="conversation"
)
nested_router.register(r"messages", MessageViewSet, basename="conversation-messages")

# URLs
urlpatterns = [
    path("", include(router.urls)),
    path("", include(nested_router.urls)),
]
