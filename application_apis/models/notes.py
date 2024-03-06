from django.db import models

class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title