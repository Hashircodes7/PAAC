from rest_framework import serializers
from audit_log.models import Audit
from decision_engine.serializers import Decision_Serializer

class Audit_Serializer(serializers.ModelSerializer):
    decision=Decision_Serializer(read_only=True)

    class Meta:
        model=Audit
        fields='__all__'