from rest_framework import serializers
from policy_engine.models import Policy

class Policy_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Policy
        fields='__all__'

    def validate(self,attrs):
        pri=attrs.get('priority')
        eff=attrs.get('effect')
        action=attrs.get('action')
        res_type=attrs.get('resource_type')

        if pri is not None:
            if pri < 0:
                raise serializers.ValidationError('Priority must be positive.')
            
        if eff is not None:
            if eff not in ['allow','deny']:
                raise serializers.ValidationError("Effect must be in  'allow' or  'deny'. ")
            
        if action is not None:
            if action not in ['read','write','update','delete']:
               raise serializers.ValidationError('Action must be read/write/update/delete.')  
                
        if res_type is not None:
            if res_type not in ['file','report','record']:
                raise serializers.ValidationError('Rescource mmust be a file/report/record.')

        return attrs
    
    
    def validate_conditions(self, value):
       
        allowed_keys = ['allowed_roles', 'min_trust_score','departments']
        
        for key in value.keys():
            if key not in allowed_keys:
                raise serializers.ValidationError(f"Invalid key in conditions: {key}")

            
            if key == 'role' and not isinstance(value[key], str):
                raise serializers.ValidationError("role must be a string")
            if key == 'trust_score' and not isinstance(value[key], int):
                raise serializers.ValidationError("trust_score must be an integer")
            
        return value