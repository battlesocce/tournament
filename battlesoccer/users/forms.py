from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django import forms


class CustomForm(forms.ModelForm):

    class Meta():
        model = CustomUser
        fields = '__all__'
        
    

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    CustomUser._meta.get_field('email')._unique = True

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields['username'].label = 'Team_login_id'
            self.fields['email'].label = 'Email Address'





