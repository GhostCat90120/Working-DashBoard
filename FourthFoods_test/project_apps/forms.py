from typing import Any
from django import forms 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Inventory


class InsertDataForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('cost_produce','cost_meat','cost_miscellaneous',)




class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name': 'username',
            'id': 'username',
            'type':'text',
            'class': 'form-input',
            'placeholder' : 'Username',
            'maxlength': '16',
            'minlength': '5'
        })
        self.fields["first_name"].widget.attrs.update({
            'required':'True',
            'name': 'first_name',
            'id': 'first_name',
            'type':'text',
            'class': 'form-input',
            'placeholder' : 'First Name',
        })
        self.fields["last_name"].widget.attrs.update({
            'required':'True',
            'name': 'last_name',
            'id': 'last_name',
            'type':'text',
            'class': 'form-input',
            'placeholder' : 'Last Name',
        })
        self.fields['email'].widget.attrs.update({ 
            'required':'True',
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'class': 'form-input', 
            'placeholder':'JohnDoe@mail.com',             
        }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password1', 
            'placeholder':'Password', 
            'maxlength':'22',  
            'minlength':'8' 
        }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password2', 
            'id':'password2', 
            'type':'password2', 
            'placeholder':'Confirm Password', 
            'maxlength':'22',  
            'minlength':'8' 
        }) 


    #first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    #last_name = forms.CharField(max_length=30, required=True)
    #email = forms.EmailField(max_length=254, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets= {
            'email':forms.TextInput(attrs={'type':'text'}),
        }