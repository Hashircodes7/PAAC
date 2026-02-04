from django.db import models
from decision_engine.models import Decision
# Create your models here.
class Audit(models.Model):
    decision=models.ForeignKey(Decision,related_name='audit_decisions',on_delete=models.SET_NULL,null=True)
    audit_time=models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.decision.user.username if self.decision and self.decision.user else 'No User'} - {self.decision.policy_used.policy_name if self.decision and self.decision.policy_used else 'No Policy'}"
