from rest_framework import serializers
from decision_engine.models import Decision
from identity_app.serializers import User_Serializer
from policy_engine.serializers import Policy_Serializer

class Decision_Serializer(serializers.ModelSerializer):
    user=User_Serializer(read_only=True)
    policy_used=Policy_Serializer(read_only=True)
    action = serializers.ChoiceField(choices=['read','write','update','delete'])
    resource = serializers.ChoiceField(choices=['file','report','record'])
    class Meta:
        model=Decision
        fields=['id','user','policy_used','action','resource','result','reason','evaluated_at']    

