from rest_framework import serializers
from .models import user, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    sender_id = serializers.CharField(source="user.user_id")

    class Meta:
        model = Message
        fields = ["message_id", "sender_id", "message_body", "sent_at"]


class ConversationSerializer(serializers.ModelSerializer):
    participants_id = UserSerializer(many=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ["conversation_id", "participants_id", "messages", "created_at"]

    def get_messages(self, obj):
        messages = obj.messages.all()
        return MessageSerializer(messages, many=True).data

    def validate(self, data):
        if not data.get("participants_id"):
            raise serializers.ValidationError("A conversation must have participants.")
        return data
