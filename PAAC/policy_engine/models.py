from django.conf import settings
from django.db import models
from django.db import models
# Create your models here.
class Policy(models.Model):
    policy_name=models.CharField(max_length=30,unique=True)
    action_choices=[('read','Read'),('write','Write'),('delete','Delete'),('update','Update')]
    action=models.CharField(max_length=10,choices=action_choices,default=None)
    resource_choices=[('report','Report'),('file','File'),('record','Record')]
    resource_type=models.CharField(max_length=10,choices=resource_choices)
    effect_choices=[('allow','Allow'),('deny','Deny')]
    effect=models.CharField(max_length=10,choices=effect_choices,default=None)
    priority=models.IntegerField()
    conditions=models.JSONField()
    is_active=models.BooleanField(default=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,  
        null=True, 
        related_name='policies_created'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='policies_updated'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    class Meta:
        unique_together = ('policy_name', 'resource_type', 'action')
 
    def __str__(self):
        return self.policy_name