from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name@example.com', 'type':'email' }), label='')