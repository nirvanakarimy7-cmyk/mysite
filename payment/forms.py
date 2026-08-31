from django import forms
from .models import shippingdress

class shippingform(forms.ModelForm):
    shipping_full_name=forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'full name :'}),
        required=True)
    
    shipping_email=forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'email :'}),
        required=True)
    
    shipping_address1=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'your first address :'}),
        required=True)
    
    shipping_address2=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'your second address :'}),
        required=False)
    
    shipping_city=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'city:'}),
        required=True)
    
    shipping_state=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'state :'}),
        required=False)
    
    shipping_zipcode=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'zipcode :'}),
        required=False)
    
    shipping_countary=forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'countary :'}),
        required=True)
    
    class Meta:
        model=shippingdress
        fields=[
    'shipping_full_name',
    'shipping_email',
    'shipping_phone',
    'shipping_address1',
    'shipping_address2',
    'shipping_city',
    'shipping_state',
    'shipping_zipcode',
    'shipping_countary',
        ]
