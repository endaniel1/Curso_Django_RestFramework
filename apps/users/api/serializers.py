from rest_framework import serializers
from apps.users.models import User

"""docstring for UserSerializer"""
class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = "__all__"