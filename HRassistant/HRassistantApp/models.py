
from django.db import models


class SecurityAuditLog(models.Model):
    event_type = models.CharField(max_length=100)
    message = models.TextField()
    risk_level = models.CharField(max_length=20, default="Low")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} - {self.risk_level}"