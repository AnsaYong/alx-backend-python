from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Message, Conversation
from serializers import MessageSerializer, ConversationSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer

    def get_queryset(self):
        return Conversation.objects.filter(participants_id=self.request.user_id)

    @action(detail=False, methods=["post"], url_path="create")
    def create_conversation(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        conversation = serializer.save(
            participants_id=[request.user_id]
        )  # Include current user as participant
        return Response(
            self.get_serializer(conversation).data, status=status.HTTP_201_CREATED
        )


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(sender_id=self.request.user_id)
