from ast import Delete
from turtle import update
from django.db import models


class TrackingEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def to_dict(self):
        return{
            'created_at': self.created_at,
            'update_at': self.update_at,
            'deleted_at': self.deleted_at
        }
        