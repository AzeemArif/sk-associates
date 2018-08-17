from django import forms


class ContactForm(forms.Form):

    Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Name'}))
    Email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Email'}))
    Subject = forms.ChoiceField(required=True,choices=[(1, 'General Customer Service'),(2, 'Suggestion'),(3, 'Product Support')], initial=1, widget=forms.Select(attrs={'class':'form-control'}))
    Message = forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder': 'Message','class':'form-control'}))