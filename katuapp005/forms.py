from django import forms
from.models import Friend

class HelloForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.CharField(label='mail', widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='age', widget=forms.NumberInput(attrs={'class':'form-control'}))
    chck = forms.BooleanField(label='Checkbox', required=False)
    check = forms.NullBooleanField(label='Check')

# class HelloForm2(forms.Form):
#     id = forms.IntegerField(label='ID')

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


#検索
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

#バリデーション
class CheckForm(forms.Form):
    str = forms.CharField(label='String', widget=forms.TextInput(attrs={'class':'form-control'}))

    #バリデーションエラーを発生させる
    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError('You input "NO"!')

    # empty = forms.CharField(label='Empty', empty_value=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    # min = forms.CharField(label='Min', min_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    # max = forms.CharField(label='Max', max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))

    #数値バリデーション
    # required = forms.IntegerField(label='Required', widget=forms.NumberInput(attrs={'class':'form-control'}))
    # min = forms.IntegerField(label='Min', min_value=100, widget=forms.NumberInput(attrs={'class':'form-control'}))
    # max = forms.IntegerField(label='Max', max_value=1000, widget=forms.NumberInput(attrs={'class':'form-control'}))

    #dateバリデーション
    # date = forms.DateField(label='Date', input_formats=['%d'], widget=forms.DateInput(attrs={'class':'form-control'}))
    # time = forms.TimeField(label='Time', widget=forms.TimeInput(attrs={'class':'form-control'}))
    # datetime = forms.DateTimeField(label='DateTime', widget=forms.DateTimeInput(attrs={'class':'form-control'}))






