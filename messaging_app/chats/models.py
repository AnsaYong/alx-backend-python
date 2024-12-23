from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class user(AbstractUser):
    ROLE_CHOICES = [
        ("guest", "Guest"),
        ("host", "Host"),
        ("admin", "Admin"),
    ]

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    password_harsh = models.CharField(max_length=128, null=False)
    phone_number = models.CharField(max_length=20, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["email"], name="unique_email")]
        indexes = [
            models.Index(fields=["email"], name="email_index"),
        ]


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender_id = models.ForeignKey(
        user.user_id, on_delete=models.CASCADE, related_name="sender"
    )
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    conversation_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    participants_id = models.ManyToManyField(user.user_id, related_name="participants")
    created_at = models.DateTimeField(auto_now_add=True)
