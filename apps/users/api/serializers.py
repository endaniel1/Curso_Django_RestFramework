from rest_framework import serializers
from apps.users.models import User

"""docstring for UserSerializer"""
class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = "__all__"

"""docstring for TestUserSerializar"""
class TestUserSerializar(serializers.Serializer):
	name = serializers.CharField(max_length = 200)
	email = serializers.EmailField()
	
	def validate_name(self, value):
		print(value)
		return value

	def validate_email(self, value):
		print(value)
		return value

	def validate(self, data):
		print("Validate General")
		return data