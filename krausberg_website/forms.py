from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'name', 'placeholder': _('contact.form.name')}))
    phone_num = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'number', 'placeholder': _('contact.form.phone')}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'email', 'placeholder': _('contact.form.email')}))
    address = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'address', 'placeholder': _('contact.form.address')}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-message-input', 'id': 'name', 'placeholder': _('contact.form.message')}))

