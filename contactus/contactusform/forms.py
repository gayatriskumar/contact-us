from django import forms
#from phonenumber_field.modelfields import PhoneNumberField
from .models import Contactusform


class Contactform(forms.ModelForm):
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_no = PhoneNumberField()
    description = forms.CharField(widget=forms.Textarea)
    """

    class Meta:
        model = Contactusform
        fields = ('id','name','email','phone_no','description')
