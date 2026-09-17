from django.contrib import admin
from .models import SecurityAuditLog


@admin.register(SecurityAuditLog)
class SecurityAuditLogAdmin(admin.ModelAdmin):
    list_display = (
        "event_type",
        "risk_level",
        "created_at",
    )

    list_filter = (
        "risk_level",
        "event_type",
    )

    search_fields = (
        "message",
    )