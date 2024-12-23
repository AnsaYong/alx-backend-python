from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r"conversations", ConversationViewSet, basename="conversations")
router.register(r"messages", MessageViewSet, basename="messages")

urlpatterns = router.urls
urlpatterns += [
    path(
        "conversations/create/",
        ConversationViewSet.as_view({"post": "create_conversation"}),
        name="create_conversation",
    ),
    path(
        "messages/<int:pk>/send/",
        MessageViewSet.as_view({"post": "send_message"}),
        name="send_message",
    ),
]
