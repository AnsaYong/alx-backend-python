from rest_framework.permissions import BasePermission


class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to check if a user is a participant in a conversation.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the logged-in user is a participant of the conversation
        return request.user in obj.participants.all()


class IsMessageSender(BasePermission):
    """
    Custom permission to allow only the sender of a message to access or modify it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the logged-in user is the sender of the message
        return obj.sender == request.user
