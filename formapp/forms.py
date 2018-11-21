from django import forms
class AddressForm(forms.Form):
    name = forms.CharField(
        label = 'Enter Your Name:',
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Name Here..'
            }
        )
    )
    father_name = forms.CharField(
        label = 'Enter Your Father Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Please enter your father name..'
            }
        )
    )
    mother_name = forms.CharField(
        label = 'Enter Your Mother Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Please enter your mother name here..'
            }
        )
    )
    mobile_number = forms.IntegerField(
        label = 'Enter Your Mobile Number:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Please enter your mobile number here..'
            }
        )
    )
    email_id = forms.EmailField(
        label = 'Enter Yor Email Id',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Please enter your emai-id here..'
            }
        )
    )
    salary = forms.IntegerField(
        label = 'Enter Your Salary',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Please enter your salary here..'
            }
        )
    )
    comm = forms.IntegerField(
        label = 'Enter Your Commission',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Please enetr commision here..'
            }
        )
    )
    location = forms.CharField(
        label = 'Enter Your Location',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Please enter your lacation here..'
            }
        )
    )

