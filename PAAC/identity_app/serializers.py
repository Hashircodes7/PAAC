from rest_framework import serializers
from identity_app.models import User

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs = {'password': {'write_only': True}}
       
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password) 
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


    def validate(self,attrs):
        exp=attrs.get('experience')
        age=attrs.get('age')
        score=attrs.get('trust_score')
 
        if exp is not None:
            if  exp < 0 or exp > 20:
                raise serializers.ValidationError('Experience is not realistic.')
        if age is not None:
            if  age < 0 or age > 100:
                raise serializers.ValidationError('Invalid age')
        if score is not None:
            if score < 0 or score > 100:
                raise serializers.ValidationError('Trust score isnt within given range(0-100)')
        
        return attrs
     