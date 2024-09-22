from rest_framework import serializers
from account.models import MyUser


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    role = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')


        if not email or not password:
            raise serializers.ValidationError(
                'Both email and password are required.')
        try:
            user = MyUser.objects.get(email=email)
            if not user.check_password(password):
                raise serializers.ValidationError('Incorrect password.')
            if user.role != role:
                raise serializers.ValidationError('Already registered with this email.')
        except MyUser.DoesNotExist:
            user = MyUser.objects.create_user(email=email,
                                              password=password, role=role)

        data['user'] = user
        return data





