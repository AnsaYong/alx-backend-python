from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
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
        indexes = [models.Index(fields=["email"], name="email_index")]
        verbose_name = "user"
        verbose_name_plural = "users"

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # Change this to a unique name
        blank=True,
        help_text="The groups this user belongs to.",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions_set",  # Change this to a unique name
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    conversation_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    participants_id = models.ManyToManyField(User, related_name="participants")
    created_at = models.DateTimeField(auto_now_add=True)
