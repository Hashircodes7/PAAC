from django.db import models
from identity_app.models import User
from policy_engine.models import Policy
# Create your models here.
class Decision(models.Model):
    user=models.ForeignKey(User,related_name='user_decisions',on_delete=models.SET_NULL,null=True)
    policy_used=models.ForeignKey(Policy,related_name='policies_decisions',on_delete=models.SET_NULL,null=True)
    action = models.CharField(max_length=10,null=True)
    resource = models.CharField(max_length=10,null=True)
    result_choices=[('allow','Allow'),('deny','Deny')]
    result=models.CharField(max_length=15,choices=result_choices,default=None)
    reason=models.TextField(max_length=150,null=True,blank=True)
    evaluated_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.user.username if self.user else 'No User'} - {self.policy_used.policy_name if self.policy_used else 'No Policy'}"
