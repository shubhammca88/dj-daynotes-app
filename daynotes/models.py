from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200, default="Untitled")
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-updated']