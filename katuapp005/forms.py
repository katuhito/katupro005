from django import forms
from.models import Friend

class HelloForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.CharField(label='mail', widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='age', widget=forms.NumberInput(attrs={'class':'form-control'}))
    chck = forms.BooleanField(label='Checkbox', required=False)
    check = forms.NullBooleanField(label='Check')

class HelloForm2(forms.Form):
    id = forms.IntegerField(label='ID')

# class HelloForm3(forms.Form):
#     name =forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control'}))
#     mail =forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
#     gender =forms.BooleanField(label='Gender', required=False, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
#     age =forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class':'form-control'}))
#     birthday = forms.DateField(label='Birth', widget=forms.DateInput(attrs={'class':'form-control'}))

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']







