from django import forms


class ContactForm(forms.Form):
    Email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Email'}))
    Message = forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder': 'Message','class':'form-control'}))