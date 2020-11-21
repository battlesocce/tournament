from rest_framework import serializers
from users.models import CustomUser
from rest_auth.serializers import PasswordResetSerializer
from allauth.account.forms import ResetPasswordForm

class PasswordSerializer (PasswordResetSerializer):
    password_reset_form_class = ResetPasswordForm

class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username",'id','is_team']