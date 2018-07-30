import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
from dictionary.models import Edge


MODEL_CHOICES = (
    ('node', ('Node')),
    ('edge', ('Edge')),
    )


class Comment(models.Model):
    model_name = models.CharField(max_length=225, choices=MODEL_CHOICES)
    model_id = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return str(self.model_name) + ": " + str(self.text)

# class Comment_To_Edge(models.Model):
#     edge = models.ForeignKey('dictionary.Edge', on_delete=models.CASCADE, related_name='comments_edge')
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)

#     def approve(self):
#         self.approved_comment = True
#         self.save()

#     def __str__(self):
#         return str(self.edge) + ": " + str(self.text)
