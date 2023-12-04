from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"E-mail", 'type':'text'}),)
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"First Name", 'type':'text'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Last Name", 'type':'text'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control validate-input'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Employee ID'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Password'
        self.fields['username'].label = 'Employee ID'
        self.fields['password2'].label = 'Confirm Password'

class CreateUserForm(forms.ModelForm):
    OPTIONS = (
            ('Employee', 'Employee'),
            ('Manager', 'Manager'),
            ('Human Resource Officer', 'Human Resource Officer'),
            ('Temp Manager', 'Temp Manager'),
            ('Admin', 'Admin'),)
    
    role = forms.ChoiceField(choices=OPTIONS, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Role'}))
    class Meta:
        model = UserProfile
        fields = ('role',)
