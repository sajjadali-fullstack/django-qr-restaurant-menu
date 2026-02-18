from django import forms


class QRCodeForm(forms.Form):
# resturant_name, resturant_url
    resturant_name = forms.CharField(
        max_length=94,
        label='Resturant Name',
        widget=forms.TimeInput(attrs={
             'class': 'form-control',  # Bootstrap deafault classes that wll help to forms look good
             'placeholder':'Enter Resturant Name',
             
        })
        )
    

    url = forms.URLField(max_length=200,
        label='Menu URL',
        widget=forms.URLInput(attrs={
        'class':'form-control',
        'placeholder':'Enter the URL of your online menu',
        })

        )
