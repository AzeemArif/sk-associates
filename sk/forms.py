from django import forms

class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True,label=False,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(required=True,label=False,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(required=True,label=False,widget=forms.Textarea(attrs={'placeholder': 'Message'}))