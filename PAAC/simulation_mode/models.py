from django.db import models
from identity_app.models import User
from decision_engine.models import Decision
# Create your models here.
class Simulation(models.Model):
    created_by=models.ForeignKey(User,related_name='createdby_simulations',on_delete=models.CASCADE)
    user_subject=models.ForeignKey(User,related_name='users_simulations',on_delete=models.CASCADE)
    decision=models.ForeignKey(Decision,on_delete=models.CASCADE,related_name='decisions_simulations',null=True,
    blank=True)
    simulated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.created_by.username} -> {self.user_subject.username}"