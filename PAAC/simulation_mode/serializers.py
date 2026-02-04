from rest_framework import serializers
from simulation_mode.models import Simulation
from identity_app.models import User

class Simulation_Serializer(serializers.ModelSerializer):
    created_by=serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model=Simulation
        fields='__all__'
        read_only_fields=['decision','simulated_at'] 

    def  validate(self,attrs):
        request_user=self.context['request'].user
        subject_user=attrs['user_subject']

        if request_user.role not in ['manager','ceo','auditor']:
            raise serializers.ValidationError('Only CEO/Manager/Auditor can make simulations.')
        
        if request_user==subject_user:
            raise serializers.ValidationError('You can not simulate yourself.')
        
        return attrs