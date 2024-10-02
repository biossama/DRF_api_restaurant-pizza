from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(min_length=8, write_only=True)
	phone_number = PhoneNumberField(allow_null=False, allow_blank=False)

	class Meta:
		model= User
		fields = ['username', 'email', 'phone_number', 'password']


	def validate_username(self, value):
		if User.objects.filter(username=value).exists():
			raise serializers.ValidationError("Ce nom d'utilisateur est déja pris, veuillez choisir un autre. ")
		return value

	def validate_email(self, value):
		if User.objects.filter(email=value).exists():
			raise serializers.ValidationError("Cet email est déja utilsé. Veuillez chosir un autre. ")
		return value

	def validate_phone_number(self, value):
		if User.objects.filter(phone_number=value).exists():
			raise serializers.ValidationError("ce numéros de téléphone est deja utilisé, Veuillez choisir un autre.  ")

		return value


	def create(self, validated_data):
		user = User.objects.create(
			username = validated_data.get('username'),
			email = validated_data.get('email'),
			phone_number = validated_data.get('phone_number')

		)

		user.set_password(validated_data.get('password'))
		user.save()

		return user
