from dateutil import parser

from rest_framework import serializers

from django.contrib.auth.models import User, Group


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):

    def validate_password(self, value):
        if value.isalnum():
            raise serializers.ValidationError('password must have atleast one special character.')
        return value

    def validate(self, data):
        if data['first_name'] == data['last_name']:
            raise serializers.ValidationError("first_name and last_name shouldn't be same.")
        return data

    def to_internal_value(self, value):
        value['date_joined'] = parser.parse(value['date_joined'])
        return super().to_internal_value(value)

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'date_joined')
        extra_kwargs = {
            'password': {'write_only': True}
        }
